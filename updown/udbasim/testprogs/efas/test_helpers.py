from EFA_v2 import *

## All programs must end with pass_test()
def parse_instructions(*args):
    efa = EFA([])
    efa.code_level = 'machine'
    state = State() 
    efa.add_initId(state.state_id)
    efa.add_state(state)

    # efa.appendBlockAction('block_pass', 'movir X16 1')
    # efa.appendBlockAction('block_pass', 'movrl X16 0(X7) 0 8')
    # efa.appendBlockAction('block_pass', 'yieldt')

    # efa.appendBlockAction('block_fail', 'movir X16 0')
    # efa.appendBlockAction('block_fail', 'movrl X16 0(X7) 0 8')
    # efa.appendBlockAction('block_fail', 'yieldt')

    def writeActions(tran, inst_arr_inner):
        for inst in inst_arr_inner:
            if isinstance(inst, list):
                writeActions(tran, inst)
                continue
            tran.writeAction(inst)

    for i in range(len(args)):
        tran = state.writeTransition('eventCarry', state, state, i)
        writeActions(tran,args[i])
        #TODO uncomment when basim supports block actions
        # tran.writeAction('fail: jmp block_fail')
        # tran.writeAction('pass: jmp block_pass')
        tran.writeAction('fail: movir X16 0')
        tran.writeAction('addi X7 X31 0')
        tran.writeAction('movrl X16 0(X31) 0 8')
        tran.writeAction('yieldt')
        tran.writeAction('pass: movir X16 1')
        tran.writeAction('addi X7 X31 0')
        tran.writeAction('movrl X16 0(X31) 0 8')
        tran.writeAction('yieldt')

    return efa

def pass_test():
    return ['jmp pass']

def fail_test():
    return ['jmp fail']

def unsigned_max_reg(reg, label=''): 
    return [f'{label}movir {reg} {unsigned_max_21}']

def unsigned_min_reg(reg,label=''):
    return [f'{label}movir {reg} {unsigned_min}']

def signed_max_reg(reg, label=''):
    return [
        f'{label}movir {reg} {unsigned_max_21}',
        f'sri {reg} {reg} 1']

def signed_min_reg(reg, label=''):
    return [
        f'{label}movir {reg} 1',
        f'sli {reg} {reg} 63']

unsigned_max_21 = 2097151
unsigned_max_16 = 65535
unsigned_max_5 = 31
unsigned_min = 0
signed_max_21 = 1048575
signed_min_21 = -1048576
signed_max_16 = 32767
signed_min_16 = -32768
signed_max_5 = 15
signed_min_5 = -16

def sanity():
    return parse_instructions(pass_test())