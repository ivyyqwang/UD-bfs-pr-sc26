from EFA_v2 import *
def sub_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-728531649697477577, 8118895529409435151]
    tran0.writeAction("movir X16 62947")
    tran0.writeAction("slorii X16 X16 12 3013")
    tran0.writeAction("slorii X16 X16 12 788")
    tran0.writeAction("slorii X16 X16 12 624")
    tran0.writeAction("slorii X16 X16 12 3127")
    tran0.writeAction("movir X17 28844")
    tran0.writeAction("slorii X17 X17 12 455")
    tran0.writeAction("slorii X17 X17 12 2014")
    tran0.writeAction("slorii X17 X17 12 3917")
    tran0.writeAction("slorii X17 X17 12 1551")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
