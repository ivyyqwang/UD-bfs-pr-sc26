from test_helpers import *

def bnei():
    x1 = 'X17'
    op = 'X8'

    def branch_to(imm, goto):
        temp = [f'bnei {x1} {imm} {goto}']
        if goto != 'fail':
            temp.append('jmp fail')
            return temp
        return temp
    
    return parse_instructions([
        f'movir {x1} 9',
        f'bnei {op} 9 pass1', #test reading op and forward traversal
        f'jmp fail', # should never run
        f'loop2: movir {x1} 8', 
        f'pass1: bnei {x1} 9 loop2', #test reverse transversal

        unsigned_max_reg(x1),
        branch_to(unsigned_max_5, 'fail'),
        unsigned_max_reg(x1),
        branch_to(signed_max_5,'pass2'),
        unsigned_max_reg(x1,'pass2: '),
        branch_to(unsigned_min, 'pass3'),
        unsigned_max_reg(x1,'pass3: '),
        branch_to(signed_min_5, 'pass4'),

        signed_max_reg(x1,'pass4: '),
        branch_to(unsigned_max_5, 'pass5'),
        signed_max_reg(x1,'pass5: '),
        branch_to(signed_max_5,'pass14'),
        signed_max_reg(x1,'pass14: '),
        branch_to(unsigned_min, 'pass6'),
        signed_max_reg(x1,'pass6: '),
        branch_to(signed_min_5, 'pass7'),

        unsigned_min_reg(x1,'pass7: '),
        branch_to(unsigned_max_5, 'pass8'),
        unsigned_min_reg(x1,'pass8: '),
        branch_to(signed_max_5,'pass9'),
        unsigned_min_reg(x1,'pass9: '),
        branch_to(unsigned_min, 'fail'),
        unsigned_min_reg(x1),
        branch_to(signed_min_5, 'pass10'),

        signed_min_reg(x1,'pass10: '),
        branch_to(unsigned_max_5, 'pass11'),
        signed_min_reg(x1,'pass11: '),
        branch_to(signed_max_5,'pass12'),
        signed_min_reg(x1,'pass12: '),
        branch_to(unsigned_min, 'pass13'),
        signed_min_reg(x1,'pass13: '),
        branch_to(signed_min_5, 'pass')
    ])
