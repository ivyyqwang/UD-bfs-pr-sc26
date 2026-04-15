from test_helpers import *


def dijkstra():
    lm_base = 'X7'
    num_vertices = 'X8'
    src = 'X9'
    uint64_max = 'X10'
    max_vertices = 'X11'
    soln_addr = 'X31'
    graph_addr = 'X30'
    dist_spt_addr = 'X29'
    v_ctr = 'X26'
    arr_idx = 'X25'
    bool_val = 'X24'
    count_ctr = 'X23'
    min = 'X22'
    min_index = 'X21'
    spt_val = 'X20'
    dist_val = 'X19'
    graph_val = 'X18'
    sum_val = 'X17'
    soln_val = 'X16'

    return parse_instructions([
        #define graph_addr, soln_addr, dist_spt_addr
        f'addi {lm_base} {graph_addr} 8',
        #soln_addr = graph_addr + (MAX_VERTICES*MAX_VERTICES*1)
        f'addi {max_vertices} {soln_addr} 0',
        f'mul {max_vertices} {soln_addr} {soln_addr}',
        f'add {graph_addr} {soln_addr} {soln_addr}',
        #dist_spt_addr = soln_addr + (MAX_VERTICES*1)
        f'addi {max_vertices} {dist_spt_addr} 0',
        f'add {soln_addr} {dist_spt_addr} {dist_spt_addr}',
        #init dist and spt loop
        f'movir {v_ctr} 0',
        f'movir {bool_val} 0',
        f'dist_spt_init_loop: bleu {num_vertices} {v_ctr} dist_spt_init_loop_exit',
        f'sli {v_ctr} {arr_idx} 4',
        f'add {dist_spt_addr} {arr_idx} {arr_idx}',
        #dist[v] = UINT64_MAX
        f'movrl {uint64_max} 0({arr_idx}) 0 8',
        #spt_set[i] = false
        f'movrl {bool_val} 8({arr_idx}) 0 8',
        f'addi {v_ctr} {v_ctr} 1',
        f'jmp dist_spt_init_loop',
        #dist[src] = 0
        f'dist_spt_init_loop_exit: movir {dist_val} 0',
        f'sli {src} {arr_idx} 4',
        f'add {dist_spt_addr} {arr_idx} {arr_idx}',
        f'movrl {dist_val} 0({arr_idx}) 0 8',
        #outer loop
        f'movir {count_ctr} 1',
        f'outer_loop: bleu {num_vertices} {count_ctr} outer_loop_exit',
        #u (min_index) = min_distance()
        f'addi {uint64_max} {min} 0',
        f'movir {v_ctr} 0',
        f'min_distance_loop: bleu {num_vertices} {v_ctr} min_distance_loop_exit',
        #get spt_set[v]
        f'sli {v_ctr} {arr_idx} 4',
        f'add {dist_spt_addr} {arr_idx} {arr_idx}',
        f'movlr 8({arr_idx}) {spt_val} 0 8',
        #if spt_set[v] == false
        f'bnei {spt_val} 0 min_distance_loop_inc',
        #then get dist[v]
        f'movlr 0({arr_idx}) {dist_val} 0 8',
        #if dist[v] <= min
        f'bgtu {dist_val} {min} min_distance_loop_inc',
        #then min = dist[v], min_index = v
        f'addi {dist_val} {min} 0',
        f'addi {v_ctr} {min_index} 0',
        f'min_distance_loop_inc: addi {v_ctr} {v_ctr} 1',
        f'jmp min_distance_loop',
        #spt_set[u] = true
        f'min_distance_loop_exit: sli {min_index} {arr_idx} 4',
        f'add {arr_idx} {dist_spt_addr} {arr_idx}',
        f'movir {spt_val} 1',
        f'movrl {spt_val} 8({arr_idx}) 0 8',
        #inner loop
        f'movir {v_ctr} 0',
        f'inner_loop: ble {num_vertices} {v_ctr} outer_loop_inc',
        #get spt_set[v]
        f'sli {v_ctr} {arr_idx} 4',
        f'add {dist_spt_addr} {arr_idx} {arr_idx}',
        f'movlr 8({arr_idx}) {spt_val} 0 8',
        #if spt_set[v] == false
        f'bneiu {spt_val} 0 inner_loop_inc',
        #then get graph[(u*vertices)+v]
        f'mul {min_index} {num_vertices} {arr_idx}',
        f'add {v_ctr} {arr_idx} {arr_idx}',
        f'add {graph_addr} {arr_idx} {arr_idx}',
        f'movlr 0({arr_idx}) {graph_val} 0 1',
        #if graph[(u*vertices)+v] > 0
        f'beqi {graph_val} 0 inner_loop_inc',
        #then get dist[u]
        f'sli {min_index} {arr_idx} 4',
        f'add {dist_spt_addr} {arr_idx} {arr_idx}',
        f'movlr 0({arr_idx}) {dist_val} 0 8',
        #if dist[u] != UINT64_MAX
        f'bequ {dist_val} {uint64_max} inner_loop_inc',
        #then get dist[u] + graph[(u*vertices)+v], dist[v]
        f'add {dist_val} {graph_val} {sum_val}',
        f'sli {v_ctr} {arr_idx} 4',
        f'add {dist_spt_addr} {arr_idx} {arr_idx}',
        f'movlr 0({arr_idx}) {dist_val} 0 8',
        #if (dist[u] + graph[(u*vertices)+v]) < dist[v]
        f'bleu {dist_val} {sum_val} inner_loop_inc',
        #then dist[v] = dist[u] + graph[(u*vertices)+v]
        f'movrl {sum_val} 0({arr_idx}) 0 8',
        f'inner_loop_inc: addi {v_ctr} {v_ctr} 1',
        f'jmp inner_loop',
        f'outer_loop_inc: addi {count_ctr} {count_ctr} 1',
        f'jmp outer_loop',
        #compare to expected
        f'outer_loop_exit: movir {v_ctr} 0',
        f'compare_loop: bge {v_ctr} {num_vertices} pass',
        #get dist[v]
        f'sli {v_ctr} {arr_idx} 4',
        f'add {arr_idx} {dist_spt_addr} {arr_idx}',
        f'movlr 0({arr_idx}) {dist_val} 0 8',
        #get soln[v]
        f'add {v_ctr} {soln_addr} {arr_idx}',
        f'movlr 0({arr_idx}) {soln_val} 0 1',
        #if dist[v] != soln[v] fail
        f'bne {dist_val} {soln_val} fail',
        f'addi {v_ctr} {v_ctr} 1',
        f'jmp compare_loop',
    ])
