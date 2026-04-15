from EFA_v2 import *
def mul_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-301780777441176105, 5095171058081696034]
    tran0.writeAction("movir X16 64463")
    tran0.writeAction("slorii X16 X16 12 3519")
    tran0.writeAction("slorii X16 X16 12 2904")
    tran0.writeAction("slorii X16 X16 12 2365")
    tran0.writeAction("slorii X16 X16 12 1495")
    tran0.writeAction("movir X17 18101")
    tran0.writeAction("slorii X17 X17 12 2801")
    tran0.writeAction("slorii X17 X17 12 1274")
    tran0.writeAction("slorii X17 X17 12 3320")
    tran0.writeAction("slorii X17 X17 12 2338")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
