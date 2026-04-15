from test_helpers import *

def bneu():
    x1 = 'X17'
    x2 = 'X18'
    op = 'X8'

    def branch_to(goto):
        temp = [f'bneu {x1} {x2} {goto}']
        if goto != 'fail':
            temp.append('jmp fail')
            return temp
        return temp
    
    return parse_instructions([
        unsigned_min_reg(x1),
        f'bneu {op} {x1} pass1', #test reading op and forward traversal
        f'jmp fail', # should never run
        f'loop2: movir {x1} 8', 
        f'pass1: bne {x1} {op} loop2', #test reverse transversal

        unsigned_max_reg(x1),
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
        branch_to('pass5'),
        signed_max_reg(x1,'pass5: '),
        signed_max_reg(x2),
        branch_to('fail'),
        signed_max_reg(x1),
        unsigned_min_reg(x2),
        branch_to('pass6'),
        signed_max_reg(x1,'pass6: '),
        signed_min_reg(x2),
        branch_to('pass7'),

        unsigned_min_reg(x1,'pass7: '),
        unsigned_max_reg(x2),
        branch_to('pass8'),
        unsigned_min_reg(x1,'pass8: '),
        signed_max_reg(x2),
        branch_to('pass9'),
        unsigned_min_reg(x1,'pass9: '),
        unsigned_min_reg(x2),
        branch_to('fail'),
        unsigned_min_reg(x1),
        signed_min_reg(x2),
        branch_to('pass10'),

        signed_min_reg(x1,'pass10: '),
        unsigned_max_reg(x2),
        branch_to('pass11'),
        signed_min_reg(x1,'pass11: '),
        signed_max_reg(x2),
        branch_to('pass12'),
        signed_min_reg(x1,'pass12: '),
        unsigned_min_reg(x2),
        branch_to('pass13'),
        signed_min_reg(x1,'pass13: '),
        signed_min_reg(x2),
        branch_to('fail'),

        unsigned_max_reg(x1),
        signed_max_reg(x2),
        branch_to('pass')
    ])
