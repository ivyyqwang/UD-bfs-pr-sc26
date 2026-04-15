from test_helpers import *

def inter_lane_comm():
    op0 = 'X8'
    op2 = 'X10'
    cont_word = 'X29'
    event_word = 'X28'
    nwid = 'X26'
    thread_id = 'X25'
    temp = 'X27'
    temp2 = 'X30'
    event_map = {
        'launch': 0,
        'launch_new_lane_same_thread': 1,
        'test_same_lane_same_thread': 2,
        'test_correct_lane_received': 3,
        'fail': 4
    }

    return parse_instructions([
        f'movir {thread_id} 1',
        #create event word for new thread
        f'loop: bgt {thread_id} {op0}  loop_exit',
        f' evi X2 {event_word} {event_map["launch_new_lane_same_thread"]} 1',
        f'ev {event_word} {event_word} {thread_id} {thread_id} 4',
        #create cont word for new lane
        f'evi {event_word} {cont_word} {event_map["test_same_lane_same_thread"]} 1',
        f'ev {cont_word} {cont_word} {thread_id} {thread_id} 8',
        #trigger event on new thread
        f'sendr_wcont {event_word} {cont_word} {thread_id} {thread_id} {op0}',
        f'addi {thread_id} {thread_id} 1',
        f'jmp loop',
        f'loop_exit: yieldt'
    ],[
        f'sri X2 {thread_id} 24',
        f'andi {thread_id} {thread_id} 255',
        #test correct thread_id
        f'bne {op0} {thread_id} fail',
        #trigger event on new lane
        f'addi {op2} {temp2} 0',
        f'sendr_reply {thread_id} {thread_id} {temp2} {temp}',
        f'yield'
    ],[
        f'sri X2 {nwid} 32',
        f'sri X2 {thread_id} 24',
        f'andi {thread_id} {thread_id} 255',
        #test caller has same thread_id
        f'bne {op0} {thread_id} fail',
        #test nwid == thread_id
        f'bne {nwid} {thread_id} fail',
        #trigger event on caller lane
        f'evi X2 {event_word} {event_map["test_correct_lane_received"]} 0 9',
        f'addi {op2} {temp2} 0',
        f'sendr {event_word} {event_word} {nwid} {nwid} {temp2} 0',
        f'yieldt'
    ],[
        #test caller nwid is same as thread_id
        f'bne {op0} {thread_id} fail',
        f'beq {op2} {thread_id} pass',
        f'yieldt'
    ],[
        fail_test()
    ])
