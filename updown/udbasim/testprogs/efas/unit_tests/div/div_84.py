from EFA_v2 import *
def div_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3474730801614995232, -2303278852247937395]
    tran0.writeAction("movir X16 53191")
    tran0.writeAction("slorii X16 X16 12 1131")
    tran0.writeAction("slorii X16 X16 12 3823")
    tran0.writeAction("slorii X16 X16 12 2580")
    tran0.writeAction("slorii X16 X16 12 224")
    tran0.writeAction("movir X17 57353")
    tran0.writeAction("slorii X17 X17 12 449")
    tran0.writeAction("slorii X17 X17 12 1617")
    tran0.writeAction("slorii X17 X17 12 377")
    tran0.writeAction("slorii X17 X17 12 3725")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
