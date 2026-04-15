from test_helpers import *

def blti():
    x1 = 'X17'
    op = 'X8'

    def branch_to(imm, goto):
        temp = [f'blti {x1} {imm} {goto}']
        if goto != 'fail':
            temp.append('jmp fail')
            return temp
        return temp
        
    
    return parse_instructions([
        f'movir {x1} 9',
        f'blti {op} 9 pass0', # test reading op
        f'jmp fail', # should never run
        f'loop2: movir {x1} 10', 
        f'pass0: blti {x1} 10 loop2', #test reverse transversal
    
        unsigned_max_reg(x1),
        branch_to(unsigned_max_5,'fail'),
        unsigned_max_reg(x1),
        branch_to(signed_max_5,'pass2'),
        unsigned_max_reg(x1,'pass2: '),
        branch_to(unsigned_min,'pass3'),
        unsigned_max_reg(x1,'pass3: '),
        branch_to(signed_min_5,'fail'),

        signed_max_reg(x1),
        branch_to(unsigned_max_5,'fail'),
        signed_max_reg(x1),
        branch_to(signed_max_5,'fail'),
        signed_max_reg(x1),
        branch_to(unsigned_min,'fail'),
        signed_max_reg(x1),
        branch_to(signed_min_5,'fail'),

        unsigned_min_reg(x1),
        branch_to(unsigned_max_5,'fail'),
        unsigned_min_reg(x1),
        branch_to(signed_max_5,'pass5'),
        unsigned_min_reg(x1,'pass5: '),
        branch_to(unsigned_min,'fail'),
        unsigned_min_reg(x1),
        branch_to(signed_min_5,'fail'),

        signed_min_reg(x1),
        branch_to(unsigned_max_5,'pass7'),
        signed_min_reg(x1,'pass7: '),
        branch_to(signed_max_5,'pass8'),
        signed_min_reg(x1,'pass8: '),
        branch_to(unsigned_min,'pass9'),
        signed_min_reg(x1,'pass9: '),
        branch_to(signed_min_5,'pass')
    ])
