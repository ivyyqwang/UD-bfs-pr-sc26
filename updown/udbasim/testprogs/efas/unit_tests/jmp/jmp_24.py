from EFA_v2 import *
def jmp_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction('jmp forward')
    tran0.writeAction('backward: movir X19 1')
    tran0.writeAction('jmp pass')
    tran0.writeAction('forward: jmp backward')
    tran0.writeAction('movir X19 0')
    tran0.writeAction('pass: addi X7 X21 0')
    tran0.writeAction('movrl X19 0(X21) 0 8')
    tran0.writeAction('movrl X19 8(X21) 0 8')
    tran0.writeAction('print: print \'%d,%d\' X19 X19')
    tran0.writeAction("yieldt")
    return efa
