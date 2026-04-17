# Introduction
This is designed to make it easier to write and run different graph algorithms.

The eventual goal is that the graph algorithms could only be specified in terms of operations on vertices and edges as well as stopping conditions.

However, currently the base code needs to be copied and updated for each algorithm.  
The following algorithms are implemented
- BFS
- PR
- Connected Components



# Compile
* The main program is located in `em.cpp` 
* Execute `make all`


# Execute
The program requires the following arguments
```
./em <graph file> <algorithm> <number of lanes> <optional algorithm argument>
current supported algorithms are BFS, CC, and PR
BFS has the following variations, BFS_PUSH_ONLY, BFS_PULL_ONLY_BASIC, BFS_PUSH_PULL_BASIC, BFS_PULL_ONLY
```
`BFS` also requires specifying the source.  `PR` requires specifying the maximum number of iterations
The graph files it currently reads are basically CSR written out in text form from ligra see `tinygraph.adj` as an example.

# How it works
The basic idea is built around a load balanced `parallel_for` for operating over (possibly complete) subsets of vertices.
The idea is as follows.
- Recursively split the current vertex subset in half
- Assign to each half a number of workers proportionally to the amount of work each half has
- Estimate the amount of work using the number of edges contained in that subset

This requires at least two base cases
- the first is when the number of vertices in the subset is 1. In this case you can evenly split the workers among the edges since there is an assumption that all edges require the same amount of processing
- the second is when the number of workers to process the subset is 1.  In this case you can simply serially iterate over the vertices and process them.

This is roughly equivalent to the following pseudocode

```python
# vertex_subset is a set of vertices, each vertex contains a prefix sum of the number of edges before it so we can estimate work fraction
# num_outgoing_edges is the number of total edges going out from the vertex subset
# num_workers is the number of workers to process this subset on
# edges_before_range is the number of edges before the subrange of vertices we are dealing with
# worker_id_start is the start of where this work should be scheduled
def parallel_for(vertex_subset, num_outgoing_edges, num_workers, edges_before_range, worker_id_start):
	if vertex_subset.size() == 1:
		# process a vertex, in parallel using num_workers
		# the work can be split evenly since each neighbor has equal amounts of work
		return process_vertex(vertex_subset[0], num_workers, worker_id_start)
	if num_workers == 1:
		# process all vertices serially on a single core
		return process_vertices_on_one_core(vertex_subset, worker_id_start)
	N = vertex_subset.size()
	middle_vertex = vertex_subset[N/2]
	edges_before = middle_vertex.edges_before - edges_before_range
	left_child_workers = ((edges_before + C*N/2)/ (M + C*N)) * num_workers
	left_child =  parallel_for(vertex_subset[0 : N/2 ], edges_before, left_child_workers, edges_before_range, worker_id_start)
	right_child = parallel_for(vertex_subset[N/2 : N], num_outgoing_edges - edges_before, num_workers - left_child_workers, middle_vertex.edges_before, worker_id_start + left_child_workers)
	return {left_child, right_child}
```

This code can be seen in all of the algorithms in `split_vertexs2`, a more complex example which does an 8 way split instead of a 2 way split can be seen in `split_vertexs`.

This in effect creates a work tree.  Each tree node has a pointer to its children and returns when both are done

# Optimizations

## Reusing the work tree
If we have multiple parallel loops over the same set of vertices we can save the work tree between iterations.  This can make later iterations cheaper since they do not need to query the work proportion and can just pass down directly to the children.

## Pruning the work tree
If we know a vertex is done being processed then we can prune that worker from the work tree.  When we return to the parent we let the parent know that they are done.  If the parent has a single child remaining it can give its parent its remaining child and prune itself.

# Push vs Pull
Many graph algorithms have two modes.
- Push Mode is when each active vertex updates its neighbors
- Pull mode is when each active vertex reads its neighbors an updates itself

Pull mode is much more efficient per vertex is processes since it does not deal with any remote writes are atomic operations.  However since it can't determine upfront the set of vertices that need to be processed it must start with all vertices.  This leads to Pull mode being better when the number of active vertices is large and push mode is better when the number of active vertices is small.

Pull mode can be implemented as described above.

Push mode is more complicated, it is described below in terms of BFS

# Algorithm specific comments

## PageRank
Page rank is the simplest algorithm.  It is simply doing the `parallel_for` above and then reusing the work tree for later iterations.

In each iteration we track the largest delta that any vertex has, this allows us to end the iterations early if we find that no delta changed by more than some epsilon.

### Implementation details 
A minor point to note about PR.  In each iteration we need to both read all of our neighbors and then write its own score. However there is no sequencing between when different vertices will read and write.  For this reason when we write not only the current score, but also the previous score and the iteration we wrote the values in.  This way other vertices can read all three values and determine which of the first two is valid for them.

## Connected Components
Connected Components also starts in Pull mode using the above `parallel_for`, however it also has some early exiting which enables work tree pruning.

In the CC algorithm each vertex starts with a label equal to its vertex id.  In each iteration each vertex reads all of its neighbors and then writes a new label with the smallest label it finds among its neighbors and itself.

As a note, in CC we do not need to be concerned with sequencing between the reads and the writes, if a different vertex reads a new label it in effect skips an iteration.

As an optimization we keep track in each iteration the smallest label globally written.  In this case we know if we ever read that smallest label we don't need to keep reading the rest of the neighbors of that vertex since it can't be smaller.  Also once a vertex writes that smallest value we know that vertex is done and can be pruned from the work tree.  This is because the smallest label globally in each iteration cannot decrease. This work pruning keeps the algorithm efficient even as the number of vertices active in each iteration gets small.


## Breadth First Search
BFS is the most complex of the three since it also includes a push mode since at the start the number of active vertices is small.

### Push Mode
There are two main difficulties in push mode
- multiple different vertices try and add the same other vertex to the next active set
- we need to prefix sums of the next active set

We handle both of these by adding additional points of global synchronization.  We use a three phase approach

- In the first phase we use the `parallel_for` to loop over all vertices in the active set and each vertex attempts to make a reservation for each of its neighbors so that it knows to update those neighbors.  A reservation is just writing to them your own vertex id so this can be checked later.  At the end exactly one of the vertex ids will be written
- In the second phase each vertex in the active set again loops over all of its neighbors and checks to see if it got any reservations.  If it got none it can be pruned.  If it got some then it prefix sums up both the number of reservations as well as the degrees.
- In between the second and third phase we have the total number of reservation, which is the number of vertices that will be in the next active set, and the number of outgoing edges, which we will need for work splitting in the next iteration
- In the third phase we once again go over the work tree and perform the write.  We can use the prefix sum over the number of reservations to be able to easily write out the frontier in parallel since we know where to write  each field and we also can write out the prefix sum over the outgoing edges to be used in the work splitting of the next iteration

We switch from push mode to pull mode when we detect that the number of edges in the next active set is greater than some constant fraction of the total edges in the graph

### Early exiting
BFS has the very simple early exiting condition in that we only need to perform a single write in each step so finding any neighbor with a set distance is enough. 




