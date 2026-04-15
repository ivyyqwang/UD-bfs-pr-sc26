from test_helpers import *

def beq():
    x1 = 'X17'
    x2 = 'X18'
    op = 'X8'

    def branch_to(goto):
        temp = [f'beq {x1} {x2} {goto}']
        if goto != 'fail':
            temp.append('jmp fail')
            return temp
        return temp
    
    return parse_instructions([
        f'beq {op} {op} pass0', # test reading op1
        f'jmp fail', # should never run
        f'loop1: movir {x1} 9', 
        f'pass0: beq {x1} {op} loop1', #test reverse transversal
    
        unsigned_max_reg(x1),
        unsigned_max_reg(x2),
        branch_to('pass1'),
        unsigned_max_reg(x1,'pass1: '),
        signed_max_reg(x2),
        branch_to('fail'),
        unsigned_max_reg(x1),
        unsigned_min_reg(x2),
        branch_to('fail'),
        unsigned_max_reg(x1),
        signed_min_reg(x2),
        branch_to('fail'),

        signed_max_reg(x1),
        unsigned_max_reg(x2),
        branch_to('fail'),
        signed_max_reg(x1,),
        signed_max_reg(x2),
        branch_to('pass2'),
        signed_max_reg(x1,'pass2: '),
        unsigned_min_reg(x2),
        branch_to('fail'),
        signed_max_reg(x1),
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
        branch_to('pass3'),
        unsigned_min_reg(x1,'pass3: '),
        signed_min_reg(x2),
        branch_to('fail'),

        signed_min_reg(x1),
        unsigned_max_reg(x2),
        branch_to('fail'),
        signed_min_reg(x1),
        signed_max_reg(x2),
        branch_to('fail'),
        signed_min_reg(x1),
        unsigned_min_reg(x2),
        branch_to('fail'),
        signed_min_reg(x1),
        signed_min_reg(x2),
        branch_to('pass')
    ])