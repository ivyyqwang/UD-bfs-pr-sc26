from EFA_v2 import *
def ceqi_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction('movir X16 -29128')
    tran0.writeAction('ceqi X16 X19 -29128')
    tran0.writeAction('ceqi X16 X20 16350')
    tran0.writeAction('addi X7 X21 0')
    tran0.writeAction('movrl X19 0(X21) 0 8')
    tran0.writeAction('movrl X20 8(X21) 0 8')
    tran0.writeAction('print: print \'%d,%d\' X19 X20')
    tran0.writeAction("yieldt")
    return efa
