from test_helpers import *

def bgei():
    x1 = 'X17'
    op = 'X8'

    def branch_to(imm, goto):
        temp = [f'bgei {x1} {imm} {goto}']
        if goto != 'fail':
            temp.append('jmp fail')
            return temp
        return temp
    
    return parse_instructions([
        f'movir {x1} 8',
        f'bgei {op} 8 pass0', # test reading op
        f'jmp fail', # should never run
        f'loop1: movir {x1} 7', 
        f'pass0: bgei {x1} 8 loop1', #test reverse traversal

        unsigned_max_reg(x1,'pass1: '),
        branch_to(unsigned_max_5,'pass8'),
        unsigned_max_reg(x1,'pass8: '),
        branch_to(signed_max_5,'fail'),
        unsigned_max_reg(x1),
        branch_to(unsigned_min,'fail'),
        unsigned_max_reg(x1),
        branch_to(signed_min_5,'pass2'),

        signed_max_reg(x1,'pass2: '),
        branch_to(unsigned_max_5,'pass3'),
        signed_max_reg(x1,'pass3: '),
        branch_to(signed_max_5,'pass10'),
        signed_max_reg(x1,'pass10: '),
        branch_to(unsigned_min,'pass4'),
        signed_max_reg(x1,'pass4: '),
        branch_to(signed_min_5,'pass5'),

        unsigned_min_reg(x1,'pass5: '),
        branch_to(unsigned_max_5,'pass6'),
        unsigned_min_reg(x1,'pass6: '),
        branch_to(signed_max_5,'fail'),
        unsigned_min_reg(x1),
        branch_to(unsigned_min,'pass9'),
        unsigned_min_reg(x1,'pass9: '),
        branch_to(signed_min_5,'pass7'),

        signed_min_reg(x1,'pass7: '),
        branch_to(unsigned_max_5,'fail'),
        signed_min_reg(x1),
        branch_to(signed_max_5,'fail'),
        signed_min_reg(x1),
        branch_to(unsigned_min,'fail'),
        signed_min_reg(x1),
        branch_to(signed_min_5,'fail'),

        unsigned_max_reg(x1),
        branch_to(signed_min_5,'pass')
    ])
