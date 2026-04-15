from EFA_v2 import *
def div_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6371929734035810721, 3917524975876589997]
    tran0.writeAction("movir X16 22637")
    tran0.writeAction("slorii X16 X16 12 2629")
    tran0.writeAction("slorii X16 X16 12 1354")
    tran0.writeAction("slorii X16 X16 12 3906")
    tran0.writeAction("slorii X16 X16 12 2465")
    tran0.writeAction("movir X17 13917")
    tran0.writeAction("slorii X17 X17 12 3459")
    tran0.writeAction("slorii X17 X17 12 1449")
    tran0.writeAction("slorii X17 X17 12 3460")
    tran0.writeAction("slorii X17 X17 12 2477")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
