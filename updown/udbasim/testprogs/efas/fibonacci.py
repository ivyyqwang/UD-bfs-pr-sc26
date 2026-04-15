from test_helpers import *

def fibonacci():
    lm_base = 'X7'
    op0 = 'X8'
    expected_result = 'X9'
    ret_value = 'X31'
    arg_value = 'X30'
    memo_size = 'X29'
    call_stack_addr = 'X28'
    memo_arr_addr = 'X27'
    store_value = 'X26'
    return_label = 'X25'
    fib_minus_1 = 'X24'
    call_arg_value = 'X23'
    memo_arr_idx = 'X22'
    call_stack_size = 'X21'
    call_stack_idx = 'X20'

    return parse_instructions([
        #define n (arg_value), call_stack mem address and depth, and memo array mem address
        f'addi {op0} {arg_value} 0',
        f'addi {lm_base} {call_stack_addr} 8',
        f'addi {lm_base} {memo_arr_addr} 376',
        f'movir {call_stack_size} 0',
        #memo_size = 2, memo[0] = 0, memo[1] = 0
        f'movir {memo_size} 2',
        f'movir {store_value} 0',
        f'movrl {store_value} 0({memo_arr_addr}) 0 4',
        f'movir {store_value} 1',
        f'movrl {store_value} 4({memo_arr_addr}) 0 4',
        #begin recursion!
        f'addi {arg_value} {call_arg_value} 0',
        f'movir {return_label} 0',  
        f'jmp call_fib',
        #if n < memo_size
        f'fib: blt {memo_size} {arg_value} not_in_memo',
        f'beq {arg_value} {memo_size} not_in_memo',
        #then
        #return memo[n]->(memo_addr + 4(n))
        f'sli {arg_value} {memo_arr_idx} 2',
        f'add {memo_arr_idx} {memo_arr_addr} {memo_arr_idx}',
        f'movlr 0({memo_arr_idx}) {ret_value} 0 4',
        f'jmp return',
        #else
        #fib(n-1)
        f'not_in_memo: subi {arg_value} {call_arg_value} 1',
        f'movir {return_label} 1',
        f'jmp call_fib',
        f'ret_fib_1: addi {ret_value} {fib_minus_1} 0',
        #fib(n-2)
        f'subi {arg_value} {call_arg_value} 2',
        f'movir {return_label} 2',
        f'jmp call_fib',
        #fib(n-1)+fib(n-2)
        f'ret_fib_2: add {ret_value} {fib_minus_1} {ret_value}',
        #push memo[n], increment memo_size, and return memo[n]
        f'sli {arg_value} {memo_arr_idx} 2',
        f'add {memo_arr_idx} {memo_arr_addr} {memo_arr_idx}',
        f'movrl {ret_value} 0({memo_arr_idx}) 0 4',
        f'addi {memo_size} {memo_size} 1',
        f'jmp return',
        #push call_stack and call fib
        f'call_fib: sli {call_stack_size} {call_stack_idx} 3',
        f'add {call_stack_idx} {call_stack_addr} {call_stack_idx}',
        f'movrl {arg_value} 0({call_stack_idx}) 0 4',
        f'movrl {return_label} 4({call_stack_idx}) 0 4',
        f'addi {call_stack_size} {call_stack_size} 1',
        f'addi {call_arg_value} {arg_value} 0',
        f'jmp fib',
        #restore call_stack and return to caller location
        f'return: subi {call_stack_size} {call_stack_size} 1', 
        f'sli {call_stack_size} {call_stack_idx} 3',
        f'add {call_stack_idx} {call_stack_addr} {call_stack_idx}',
        f'movlr 0({call_stack_idx}) {arg_value} 0 4',
        f'movlr 4({call_stack_idx}) {return_label} 0 4',
        # fib_minus_1 will equal memo[arg_value-1] if it's been calculated
        f'subi {arg_value} X17 1',
        f'sli X17 {memo_arr_idx} 2',
        f'add {memo_arr_idx} {memo_arr_addr} {memo_arr_idx}',
        f'movlr 0({memo_arr_idx}) {fib_minus_1} 0 4',
        f'beqi {return_label} 1 ret_fib_1',
        f'bgti {return_label} 1 ret_fib_2',
        #verify result 
        f'bne {ret_value} {expected_result} fail',
        pass_test()
    ])

#mem map:
#0:7 test word
#8:375 call_stack
#376:559 memo_arr