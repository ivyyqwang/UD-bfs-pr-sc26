from test_helpers import *

def single_lane_multi_thread_init():
    op0 = 'X8'
    op1 = 'X9'
    x1 = 'X17'
    event_map = {
        "thread_initiator": 0,
        'check_thread_count': 1}
    
    return parse_instructions([
        f'blei {op0} 1 pass',
        f'movir {x1} 1',
        f'movir X16 0',
        f'loop: evii X16 {event_map["check_thread_count"]} 255 5',
        f'addi {x1} {x1} 1',
        f'sendr X16 X2 {op0} {x1} {x1} 1',
        f'bgt {op0} {x1} loop',
        'yield'
    ],[
        f'beq {op0} {op1} pass',
        f'bgt {op1} {op0} fail',
        'yield'
    ])