from EFA_v2 import *
def add_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3755217364194611913, 6678761497565979317]
    tran0.writeAction("movir X16 52194")
    tran0.writeAction("slorii X16 X16 12 3227")
    tran0.writeAction("slorii X16 X16 12 1032")
    tran0.writeAction("slorii X16 X16 12 3282")
    tran0.writeAction("slorii X16 X16 12 3383")
    tran0.writeAction("movir X17 23727")
    tran0.writeAction("slorii X17 X17 12 2979")
    tran0.writeAction("slorii X17 X17 12 585")
    tran0.writeAction("slorii X17 X17 12 3998")
    tran0.writeAction("slorii X17 X17 12 693")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
