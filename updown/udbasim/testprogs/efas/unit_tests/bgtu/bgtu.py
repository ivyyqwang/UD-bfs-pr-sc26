from test_helpers import *

def bgtu():
    x1 = 'X17'
    x2 = 'X18'
    op = 'X8'

    def branch_to(goto):
        temp = [f'bgtu {x1} {x2} {goto}']
        if goto != 'fail':
            temp.append('jmp fail')
            return temp
        return temp
    
    return parse_instructions([
        f'movir {x1} 7',
        f'bgt {op} {x1} pass0', # test reading op
        f'jmp fail', # should never run
        f'loop2: movir {x1} 9', 
        f'bgt {x1} {op} pass1', #exit loop
        f'pass0: jmp loop2',#test reverse transversal

        unsigned_max_reg(x1,'pass1: '),
        unsigned_max_reg(x2),
        branch_to('fail'),
        unsigned_max_reg(x1),
        signed_max_reg(x2),
        branch_to('pass2'),
        unsigned_max_reg(x1,'pass2: '),
        unsigned_min_reg(x2),
        branch_to('pass3'),
        unsigned_max_reg(x1,'pass3: '),
        signed_min_reg(x2),
        branch_to('pass4'),

        signed_max_reg(x1,'pass4: '),
        unsigned_max_reg(x2),
        branch_to('fail'),
        signed_max_reg(x1),
        signed_max_reg(x2),
        branch_to('fail'),
        signed_max_reg(x1),
        unsigned_min_reg(x2),
        branch_to('pass5'),
        signed_max_reg(x1,'pass5: '),
        signed_min_reg(x2),
        branch_to('fail'),

        unsigned_min_reg(x1),
        unsigned_max_reg(x2),
        branch_to('fail'),
        unsigned_min_reg(x1),
        signed_max_reg(x2),
        branch_to('fail'),
        unsigned_min_reg(x1),
        unsigned_min_reg(x2),
        branch_to('fail'),
        unsigned_min_reg(x1),
        signed_min_reg(x2),
        branch_to('fail'),

        signed_min_reg(x1),
        unsigned_max_reg(x2),
        branch_to('fail'),
        signed_min_reg(x1),
        signed_max_reg(x2),
        branch_to('pass7'),
        signed_min_reg(x1,'pass7: '),
        unsigned_min_reg(x2),
        branch_to('pass8'),
        signed_min_reg(x1,'pass8: '),
        signed_min_reg(x2),
        branch_to('fail'),
        pass_test()
    ])
