from EFA_v2 import *
def div_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3050575999644903363, 6600530711817050818]
    tran0.writeAction("movir X16 54698")
    tran0.writeAction("slorii X16 X16 12 724")
    tran0.writeAction("slorii X16 X16 12 2684")
    tran0.writeAction("slorii X16 X16 12 3413")
    tran0.writeAction("slorii X16 X16 12 2109")
    tran0.writeAction("movir X17 23449")
    tran0.writeAction("slorii X17 X17 12 3259")
    tran0.writeAction("slorii X17 X17 12 1558")
    tran0.writeAction("slorii X17 X17 12 3733")
    tran0.writeAction("slorii X17 X17 12 2754")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
