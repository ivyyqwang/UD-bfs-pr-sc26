from test_helpers import *

def cgti():
    xs = 'X17'
    xd = 'X19'
    op = 'X8'

    def compare_and_branch(expected, imm):
        return [
            f'cgti {xs} {xd} {imm}',
            f'bnei {xd} {expected} fail']
    
    return parse_instructions([
        f'cgti {op} {xd} 7',
        f'bnei {xd} 1 fail',
        f'cgti {op} {xd} 8',
        f'bnei {xd} 0 fail',

        unsigned_max_reg(xs),
        compare_and_branch(0, unsigned_max_16),
        unsigned_max_reg(xs),
        compare_and_branch(0, signed_max_16),
        unsigned_max_reg(xs),
        compare_and_branch(0, unsigned_min),
        unsigned_max_reg(xs),
        compare_and_branch(1, signed_min_16),

        signed_max_reg(xs),
        compare_and_branch(1, unsigned_max_16),
        signed_max_reg(xs),
        compare_and_branch(1, signed_max_16),
        signed_max_reg(xs),
        compare_and_branch(1, unsigned_min),
        signed_max_reg(xs),
        compare_and_branch(1, signed_min_16),

        unsigned_min_reg(xs),
        compare_and_branch(1, unsigned_max_16),
        unsigned_min_reg(xs),
        compare_and_branch(0, signed_max_16),
        unsigned_min_reg(xs),
        compare_and_branch(0, unsigned_min),
        unsigned_min_reg(xs),
        compare_and_branch(1, signed_min_16),

        signed_min_reg(xs),
        compare_and_branch(0, unsigned_max_16),
        signed_min_reg(xs),
        compare_and_branch(0, signed_max_16),
        signed_min_reg(xs),
        compare_and_branch(0, unsigned_min),
        signed_min_reg(xs),
        compare_and_branch(0, signed_min_16),

        pass_test()
    ])