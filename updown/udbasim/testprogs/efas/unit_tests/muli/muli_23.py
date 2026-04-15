from EFA_v2 import *
def muli_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8061719179524995415, 27349]
    tran0.writeAction("movir X16 36895")
    tran0.writeAction("slorii X16 X16 12 81")
    tran0.writeAction("slorii X16 X16 12 3705")
    tran0.writeAction("slorii X16 X16 12 1880")
    tran0.writeAction("slorii X16 X16 12 1705")
    tran0.writeAction("muli X16 X17 27349")
    tran0.writeAction("yieldt")
    return efa
