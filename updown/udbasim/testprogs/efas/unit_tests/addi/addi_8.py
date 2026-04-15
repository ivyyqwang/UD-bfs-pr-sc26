from EFA_v2 import *
def addi_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-661762263559915135, 23200]
    tran0.writeAction("movir X16 63184")
    tran0.writeAction("slorii X16 X16 12 3883")
    tran0.writeAction("slorii X16 X16 12 2618")
    tran0.writeAction("slorii X16 X16 12 3083")
    tran0.writeAction("slorii X16 X16 12 2433")
    tran0.writeAction("addi X16 X17 23200")
    tran0.writeAction("yieldt")
    return efa
