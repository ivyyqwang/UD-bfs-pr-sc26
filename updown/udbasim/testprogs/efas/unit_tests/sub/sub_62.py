from EFA_v2 import *
def sub_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8930043978597593460, -6966482343695508923]
    tran0.writeAction("movir X16 33810")
    tran0.writeAction("slorii X16 X16 12 453")
    tran0.writeAction("slorii X16 X16 12 155")
    tran0.writeAction("slorii X16 X16 12 304")
    tran0.writeAction("slorii X16 X16 12 3724")
    tran0.writeAction("movir X17 40786")
    tran0.writeAction("slorii X17 X17 12 339")
    tran0.writeAction("slorii X17 X17 12 2025")
    tran0.writeAction("slorii X17 X17 12 4089")
    tran0.writeAction("slorii X17 X17 12 2629")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
