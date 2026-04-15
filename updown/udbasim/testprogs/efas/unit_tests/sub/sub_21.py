from EFA_v2 import *
def sub_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7312254749405770886, -4982662024895540819]
    tran0.writeAction("movir X16 39557")
    tran0.writeAction("slorii X16 X16 12 2672")
    tran0.writeAction("slorii X16 X16 12 3106")
    tran0.writeAction("slorii X16 X16 12 2072")
    tran0.writeAction("slorii X16 X16 12 2938")
    tran0.writeAction("movir X17 47834")
    tran0.writeAction("slorii X17 X17 12 116")
    tran0.writeAction("slorii X17 X17 12 2466")
    tran0.writeAction("slorii X17 X17 12 1117")
    tran0.writeAction("slorii X17 X17 12 429")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
