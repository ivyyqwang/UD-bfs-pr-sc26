
import os 
import numpy as np 
from scipy.sparse import rand, coo_matrix, tril 
from sklearn.neighbors import BallTree
from random import shuffle#, randint


#
#   Drivers
#

def generate_n_write_RMAT(outdir,scale,seed=0,a=.57,b=.19,c=.19,avg_degree=16,clip_n_flip=False):

    assert outdir[-1] == '/'
    assert os.path.isdir(outdir)
    assert (a + b + c) <= 1.0 

    return_lower_triangular=True

    #filename = f"RMAT_a:{a}_b:{b}_c:{c}_avgDegree:{avg_degree}_clipnflip:{clip_n_flip}_scale:{scale}_onlyLowerTriangular:{return_lower_triangular}_seed:{seed}_edges.txt"
    filename = f"RMAT_scale_{scale}_seed_{seed}_edges.txt"
    A = RMAT_coo_mat(scale, avg_degree, a, b, c, seed, clip_n_flip,return_lower_triangular=return_lower_triangular)

    with open(outdir + filename,"w") as f:    
        for (i,j) in zip(*A.nonzero()):
            f.write(f"{i} {j}\n")

    return A, filename

 

def generate_n_write_ER(outdir,n, p=None, seed=0):
    """
        Method generates a symmetric COO matrix of dimension n, with density p.
        File written has a header with the number of rows (n), columns (n), and
        the number of edges (m). Following the header are the edges of the graph
        with indices delimited by a space.
    """


    assert outdir[-1] == '/'
    assert os.path.isdir(outdir)

    if p is None:
        p = np.log(n)/n # default is set to make graph connected
    assert 0.0 < p <= 1.0 

    #if seed is not None: 
    #    np.random.seed(seed)

    if seed is None:
        filename = f"ER_n:{n}_p:{p}_coo.smat"
    else:
        filename = f"ER_n:{n}_p:{p}_seed:{seed}_coo.smat"

    A = ER(n,p,seed)
    save_edge_file(outdir +filename, A)

    return A, filename

def generate_n_write_large_ER(outdir,n, p=None, seed=0):
    assert outdir.endswith('/')
    assert os.path.isdir(outdir)

    if p is None:
        p = np.log(n) / n   # 经典连通阈值
    assert 0.0 < p <= 1.0

    rng = np.random.default_rng(seed)

    # 期望无向边数
    m = int(p * n * (n - 1) // 2)

    filename = f"{outdir}ER_n:{n}_p:{p:.3e}_seed:{seed}_coo.smat"

    with open(filename, "w") as f:
        edges = set()
        batch = max(1_000_000, m // 10)

        while len(edges) < m:
            k = min(batch, m - len(edges))

            u = rng.integers(0, n, size=k, dtype=np.int64)
            v = rng.integers(0, n, size=k, dtype=np.int64)

            mask = u != v
            u, v = u[mask], v[mask]

            a = np.minimum(u, v)
            b = np.maximum(u, v)

            for x, y in zip(a, b):
                edges.add((x, y))

        # 写成对称 COO
        for x, y in edges:
            f.write(f"{x} {y}\n")
            f.write(f"{y} {x}\n")

def generate_same_degree(outdir, n, avg_deg=16,seed=0):
    assert outdir.endswith('/')
    assert os.path.isdir(outdir)

    filename = f"{outdir}fix_deg_n:{n}_deg:{avg_deg}_seed:{seed}.smat"
    rng = np.random.default_rng(seed)

    with open(filename, "w") as f:
        for x in range(0, n):
            u = rng.integers(0, n, size=avg_deg, dtype=np.int64)
            for y in u:
                f.write(f"{x} {y}\n")



def generate_n_write_nn_graph(X, outdir, search_param, seed=0, use_radius=False):
    """-------------------------------------------------------------------------
      Method generates a symmetric n x n COO matrix, from the nearest neighbors
    of the input embedding array X. search_param is either the number of 
    neighbors to query, or a fixed radius to search each point. File written has
    a header with the number of rows (n), columns (n), and the number of edges 
    (m). Following the header are the edges of the graph with indices delimited
    by a space.
    -------------------------------------------------------------------------"""


    assert outdir[-1] == '/'
    assert os.path.isdir(outdir)

    assert search_param > 0 

    file_prefix = f"KNN_n:{n}_"

    if use_radius:
        assert isinstance(search_param, float)
        file_prefix += f"r:{search_param}_"
    else:
        assert isinstance(search_param, int)
        file_prefix += f"k:{search_param}_"

    if seed is not None:
        file_prefix += f"seed:{seed}_"

    output_file = outdir + file_prefix + "coo.smat"
    A = knn(X,search_param,seed)
    save_edge_file(output_file, A)
    return A, output_file


def generate_n_write_forest_fire_graph(outdir, n : int, seed_clique_size : int = 10, burn_p : float = .4, seed=0):
    assert outdir[-1] == '/'
    assert os.path.isdir(outdir)
    assert 0 < burn_p <= 1 

    file_prefix = f"FF_n:{n}_seedSize:{seed_clique_size}_p:{burn_p}"

    if seed is not None:
        file_prefix += f"seed:{seed}_"

    output_file = outdir + file_prefix + "coo.smat"
    A,_ = forest_fire_graph(n, seed_clique_size, burn_p, seed)
    save_edge_file(output_file, A)

    return A, output_file

#
#   FileIO 
#

def save_edge_file(filename, A, delimiter=" "):
    n,n = A.shape
    with open(filename,"w") as f:   
        f.write(f"{n} {n} {A.nnz}\n")
        for (i,j) in zip(*A.nonzero()):
            f.write(f"{i}{delimiter}{j}\n")

def load_edge_file(filename,delimiter=" "):
    
    n,nnzs = -1, -1
    Is, Js = [], []
    with open(filename,"r") as f: 
        header = f.readline()
        n,_, nnzs = header.rstrip().split(delimiter)
        n = int(n)
        nnzs = int(nnzs)
        Is = np.empty(nnzs)    
        Js = np.empty(nnzs)   

        for (idx,line) in enumerate(f): 
            i, j = line.rstrip().split(delimiter)
            Is[idx] = int(i)
            Js[idx] = int(j)

    return coo_matrix((np.ones(nnzs),(Is,Js)),shape=(n,n))

#
#   Graph Generators
#

#  -- RMAT Graphs

def RMAT_coo_mat(*args, return_lower_triangular=False):

    n, m, Is, Js = RMAT(*args)     

    A = coo_matrix((np.ones(m),(Is,Js)),shape=(n,n))
    A = coo_matrix(A + A.T)
    A.sum_duplicates()
    A.data[:]=1
    if return_lower_triangular:
        return tril(A)
    else:
        return A 

def RMAT(scale, avg_deg=16, a = .57, b = .19, c = .19, seed=None, clip_n_flip=False):
    #graph 500 specifications

    if seed is not None: 
        np.random.seed(seed)

    n = 2**scale 

    m = int(avg_deg*n)

    Is = np.ones(m,dtype=np.int64)
    Js = np.ones(m,dtype=np.int64)

    ab = a + b
    c_norm = c/(1 - ab)
    a_norm = a/ab

    for ib in range(1,scale+1):
        
        for e_idx in range(m):
            i_bit = np.random.rand() > ab

            if i_bit:
                val_check = c_norm
            else: 
                val_check = a_norm
            j_bit = np.random.rand() > val_check#((c_norm if i_bit else 0.0) + (a_norm if not(i_bit) else 0.0))

            if i_bit:
                Is[e_idx] += 2**(ib-1)
            
            if j_bit:
                Js[e_idx] += 2**(ib-1)

    p = np.random.permutation(n)

    for e_idx in range(m):
        Is[e_idx] = p[Is[e_idx]-1]
        Js[e_idx] = p[Js[e_idx]-1]

    if clip_n_flip:
        #from (section 3.4,R-MAT: A Recursive Model for Graph Mining  Chakrabarti et al.)
        
        new_edge_count = 0
        for e_idx in range(m):
            if Is[e_idx] < Js[e_idx]:
                new_edge_count += 2 
            # get rid of self loops

        new_Is = np.empty(new_edge_count,dtype=np.int64)
        new_Js = np.empty(new_edge_count,dtype=np.int64)
        new_idx = 0

        for e_idx in range(m):

            if Is[e_idx] < Js[e_idx]:

                new_Is[new_idx] = Is[e_idx]
                new_Js[new_idx] = Js[e_idx]
                new_idx += 1

                new_Is[new_idx] = Js[e_idx]
                new_Js[new_idx] = Is[e_idx]
                new_idx += 1

        return n, new_edge_count, new_Is, new_Js  
    else:
        new_edge_count = 0
        for e_idx in range(m):
            if Is[e_idx] != Js[e_idx]:
                new_edge_count += 1 
            # get rid of self loops

        new_Is = np.empty(new_edge_count,dtype=np.int64)
        new_Js = np.empty(new_edge_count,dtype=np.int64)
        new_idx = 0 
        for e_idx in range(m):

            if Is[e_idx] != Js[e_idx]:

                new_Is[new_idx] = Is[e_idx]
                new_Js[new_idx] = Js[e_idx]
                new_idx += 1

        return n, new_edge_count, new_Is, new_Js  





#  -- ER Graphs

def ER(n,p,seed=None):
    if seed is not None:
        np.random.seed(seed)
    A = rand(n,n,p)
    A = A + A.T # symmetrize 
    A.data[:] = 1 

    return A 


#  -- Nearest Neighbor Graphs

def generate_embeddings(n : int, d : int, distribution):
    """-------------------------------------------------------------------------
        Generate random n x d embeddings, with the expectation that n >> d. 
      These are used in tandem with the knn graphs. 
    -------------------------------------------------------------------------""" 
    pass

def knn(X : np.array, k: int, seed = None):
    if seed is not None:
        np.random.seed(seed)

    n, d = X.shape # expecting tall skinny matrix 
    assert n >= d 
    X_tree =  BallTree(X)
    Is = np.empty(n*d,np.int)
    Js = np.empty(n*d,np.int)
    
    edge_idx = 0 
    for i in range(n):
        _, indices = X_tree.query(X[i,:], k=k)
        for j in range(k):
            Is[edge_idx] = indices[i]
            Js[edge_idx] = indices[j]
            edge_idx += 1 

    A = coo_matrix((np.ones(n*d), (Is,Js)), shape=(n,n))
    A = A + A.T 
    A.data[:] = 1 

    return A 

def knn(X : np.array, r: float, seed = None):
    if seed is not None:
        np.random.seed(seed)

    n, d = X.shape # expecting tall skinny matrix 
    assert n >= d 
    X_tree =  BallTree(X)
    Is = []
    Js = []
    
    edge_idx = 0 
    for i in range(n):
        indices = X_tree.query_radius(X[i,:],r,return_distance=False)

        Is.extend([i]*len(indices))
        Js.extend(indices)

    A = coo_matrix((np.ones(len(Is)), (Is,Js)), shape=(n,n))
    A = A + A.T 
    A.data[:] = 1 

    return A 

#  -- Forest Fire Graphs 

def forest_fire_graph(target_size : int, m: int = 10, burn_p: float =.4, seed = None):

    if seed is not None:
        #print(f"seeding with seed:{seed} with burn_p:{burn_p}")
        np.random.seed(seed)
        
    clique = rand(m,m,1.0)
    clique.setdiag(0.0)
    clique.eliminate_zeros()
    return forest_fire_graph_from_seed(clique, target_size, burn_p)

def forest_fire_graph_from_seed(seed_network, target_size : int, burn_p : float):

    graph_size = seed_network.shape[0]
    steps = target_size - graph_size
    parents = [-1 for i in range(target_size)]
    for i in range(graph_size):
        parents[i] = i 

    toburn = set()
    burnt = set()
    burning = set()
    alive = []


    #  -- convert seed_graph to List of Lists format -- #
    neighbors = matrix_to_list_of_list(seed_network) # assuming symmetric network
    for _ in range(steps):
        neighbors.append([]) # add in entries for new nodes 

    for v_i in range(seed_network.shape[0],target_size):
        parent = np.random.randint(0,graph_size)

        new_v = graph_size#+1 #NOTE: should this be + 1 
        burn_(neighbors,neighbors[new_v],parent,burn_p,
              toburn,burnt,burning,alive)
        toburn.clear()
        burnt.clear()
        burning.clear()
        alive.clear()


        parents[v_i] = parent
        graph_size += 1

        #symmetrize the neighbor list with the new neighbors of new_v
        for v_j in neighbors[new_v]:
            neighbors[v_j].append(new_v)

    return list_of_list_to_matrix(neighbors), parents

def burn_(A, walked_edges : list, v0 : int, p : float): 
    """ TODO: update the documentation 
    `burn!`
    =======
    Update the array `walked_edges` with vertices traversed in a random walk (a.k.a
    "burning") starting from `v0` in `A`. `A` is either a MatrixNetwork or a edge 
    list representation. The number of edges selected at each step of the walk is
    determined by a geometric distribution with success rate `p`.

    Input
    -----
    - `neighbor::Union{Vector{Vector{S}},MatrixNetwork{T}}`: The graph being walked.
    - `walked_edges::Vector{S}`: Array to store the vertices visited on the walk. 
    - `v0 <: Integer`: The starting vertex of the random walk. 
    - `p::Float64`: The geometric distribution's success probability for selecting
    the edges in the random walk. 

    Functions
    ---------
    * `burn!(A,walked_edges,v0,p)` Same as below, but returns initialized variables
    for reuse (fewer allocations). 
    * burn!(A,walked_edges,v0,p,toburn,burnt,burning,alive) Updates the Array 
    `walked_edges` with vertices visted from a random walk starting at `v0`, which
    keeps edges proportional to geomdist(`p`). `toburn`, `burnt`, `burning`,and 
    `alive` are variables used for running the walk, and are returned for reuse if
    the routine is going to be run multiple times. These variables have no 
    assumption of their contents and have `empty!` called on them at the beginning
    of the routine. 
    """
    toburn = set()
    burnt = set()
    burning = set()
    alive = []
    burn_(A,walked_edges,v0,p,toburn,burnt,burning,alive)

#TODO: add type to A
def burn_(A, walked_edges : list, v0 : int, p : float,
          toburn : set , burnt : set, burning :set, alive : list):
    walked_edges.append(v0)
    toburn.add(v0)
    burnt.add(v0)

    while (len(toburn) > 0):
        # -- burning = toburn -- # 
        burning.clear()
        for v in toburn:
            burning.add(v)
 
        toburn.clear()

        # -- randomly walk v's edges, visited nodes become v_new's neighbors -- # 
        for v in burning:

            alive.clear()

            for j in A[v]:
                if j not in burnt:
                    alive.append(j)


            if len(alive) > 0: #add `#' of survivors to v_new's neighbor list

                np.random.shuffle(alive)

                y = int(np.floor(np.log(np.random.random())/np.log(p))) 
                             # geometric_dist(1-p)
                new_edges = min(y, len(alive))

                for i in range(new_edges):
                    toburn.add(alive[i])
                    burnt.add(alive[i])
                    walked_edges.append(alive[i])

def matrix_to_list_of_list(A):
    n,_ = A.shape
    list_of_list_representation = [[] for _ in range(n)]

    for (i,j) in zip(*A.nonzero()):# A is expected to be symmetric
        list_of_list_representation[i].append(j)
    
    return list_of_list_representation

def list_of_list_to_matrix(list_of_lists):
    
    n = len(list_of_lists)
    nonzeros = sum([len(l) for l in list_of_lists])

    Is = np.empty(nonzeros,int)
    Js = np.empty(nonzeros,int)
    edge_idx = 0 
    for i in range(n):
        for j in list_of_lists[i]:
            Is[edge_idx] = i 
            Js[edge_idx] = j 
            edge_idx += 1 
    
    A = coo_matrix((np.ones(len(Is)), (Is,Js)), shape=(n,n))
    return A.tocsr()

import sys
if __name__ == "__main__":
    # generate_n_write_large_ER("./", int(sys.argv[1]))
    # generate_same_degree("./", int(sys.argv[1]))
    generate_n_write_large_ER("./", 1 << int(sys.argv[1]))
    generate_n_write_forest_fire_graph("./", 1 << int(sys.argv[1]))
    generate_n_write_RMAT("./", int(sys.argv[1]))

