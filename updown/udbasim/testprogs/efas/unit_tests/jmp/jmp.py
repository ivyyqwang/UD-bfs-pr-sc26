from test_helpers import *

def jmp():
    return parse_instructions([
        'jmp forward',
        'jmp fail',
        'backward: jmp pass',
        'jmp fail',
        'forward: jmp backward',
        'jmp fail',
        pass_test()
    ])