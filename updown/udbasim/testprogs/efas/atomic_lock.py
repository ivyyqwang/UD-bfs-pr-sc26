from test_helpers import *

def atomic_lock():
    lm_base = 'X7'
    lock_bool = 'X31'
    atomic_value = 'X30'
    lock_addr = 'X27'
    is_laneA = 'X29'
    loop_ctr = 'X28'

    return parse_instructions([
        # get lock_addr
        f'addi {lm_base} {lock_addr} 8',
        # spin lock
        f'spin_loop1: cswpi {lock_bool} {lock_addr} 0 1',
        f'bnei {lock_bool} 0 spin_loop1',
        # read atomic value
        f'movlr 8({lock_addr}) {atomic_value} 0 8',
        f'bnei {atomic_value} 0 shift1',
        # if atomic value is 0 set 2, laneA only
        f'movir {atomic_value} 2',
        f'movrl {atomic_value} 8({lock_addr}) 0 8',
        f'movir {is_laneA} 1',
        f'jmp release_lock',
        # if atomic value is not 0 shift left, laneB only
        f'shift1: sli {atomic_value} {atomic_value} 1',
        f'movrl {atomic_value} 8({lock_addr}) 0 8',
        f'movir {is_laneA} 0',
        # release lock
        f'release_lock: movir {lock_bool} 0',
        f'movrl {lock_bool} 0({lock_addr}) 0 8',
        f'beq {is_laneA} 1 do_busy_loop',
        # laneB ends here
        f'yield',
        # laneA continues
        f'do_busy_loop: movir {loop_ctr} 0',
        f'busy_loop: addi {loop_ctr} {loop_ctr} 1',
        f'blti {loop_ctr} 5 busy_loop',
        # spin lock
        f'spin_loop2: cswpi {lock_bool} {lock_addr} 0 1',
        f'bnei {lock_bool} 0 spin_loop2',
        # read and release
        f'movlr 8({lock_addr}) {atomic_value} 0 8',
        f'movir {lock_bool} 0',
        f'movrl {lock_bool} 0({lock_addr}) 0 8',
        # verify shift
        f'movlr 8({lock_addr}) {atomic_value} 0 8',
        f'bnei {atomic_value} 4 fail',
        pass_test()
    ])

#laneA                #laneB
#spin lock            #spin lock
#val = 2         
#release lock 
#wait 10 cycles       #val *= 2     
#spin lock            #release lock
#test val == 4