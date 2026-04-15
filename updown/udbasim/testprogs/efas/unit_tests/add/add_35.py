from EFA_v2 import *
def add_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5074325636217486165, 7888745550467511333]
    tran0.writeAction("movir X16 47508")
    tran0.writeAction("slorii X16 X16 12 1531")
    tran0.writeAction("slorii X16 X16 12 2050")
    tran0.writeAction("slorii X16 X16 12 2452")
    tran0.writeAction("slorii X16 X16 12 1195")
    tran0.writeAction("movir X17 28026")
    tran0.writeAction("slorii X17 X17 12 1860")
    tran0.writeAction("slorii X17 X17 12 2083")
    tran0.writeAction("slorii X17 X17 12 243")
    tran0.writeAction("slorii X17 X17 12 1061")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
