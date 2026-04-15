from test_helpers import *

def cgt():
    xs = 'X17'
    xt = 'X18'
    xd = 'X19'
    op = 'X8'

    def compare_and_branch(expected):
        return [
            f'cgt {xs} {xt} {xd}',
            f'bnei {xd} {expected} fail']
    
    return parse_instructions([
        unsigned_min_reg(xt),
        f'cgt {op} {xt} {xd}',
        f'bnei {xd} 1 fail',
        f'cgt {xt} {op} {xd}',
        f'bnei {xd} 0 fail',

        unsigned_max_reg(xs),
        unsigned_max_reg(xt),
        compare_and_branch(0),
        unsigned_max_reg(xs),
        unsigned_min_reg(xt),
        compare_and_branch(0),
        unsigned_max_reg(xs),
        signed_max_reg(xt),
        compare_and_branch(0),
        unsigned_max_reg(xs),
        signed_min_reg(xt),
        compare_and_branch(1),

        signed_max_reg(xs),
        unsigned_max_reg(xt),
        compare_and_branch(1),
        signed_max_reg(xs),
        unsigned_min_reg(xt),
        compare_and_branch(1),
        signed_max_reg(xs),
        signed_max_reg(xt),
        compare_and_branch(0),
        signed_max_reg(xs),
        signed_min_reg(xt),
        compare_and_branch(1),

        unsigned_min_reg(xs),
        unsigned_max_reg(xt),
        compare_and_branch(1),
        unsigned_min_reg(xs),
        unsigned_min_reg(xt),
        compare_and_branch(0),
        unsigned_min_reg(xs),
        signed_max_reg(xt),
        compare_and_branch(0),
        unsigned_min_reg(xs),
        signed_min_reg(xt),
        compare_and_branch(1),

        signed_min_reg(xs),
        unsigned_max_reg(xt),
        compare_and_branch(0),
        signed_min_reg(xs),
        unsigned_min_reg(xt),
        compare_and_branch(0),
        signed_min_reg(xs),
        signed_max_reg(xt),
        compare_and_branch(0),
        signed_min_reg(xs),
        signed_min_reg(xt),
        compare_and_branch(0),
        pass_test()
    ])
