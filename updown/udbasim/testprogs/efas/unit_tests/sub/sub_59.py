from EFA_v2 import *
def sub_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5159454150111944827, 609547369836487672]
    tran0.writeAction("movir X16 47205")
    tran0.writeAction("slorii X16 X16 12 3836")
    tran0.writeAction("slorii X16 X16 12 2387")
    tran0.writeAction("slorii X16 X16 12 2713")
    tran0.writeAction("slorii X16 X16 12 3973")
    tran0.writeAction("movir X17 2165")
    tran0.writeAction("slorii X17 X17 12 2241")
    tran0.writeAction("slorii X17 X17 12 2676")
    tran0.writeAction("slorii X17 X17 12 3594")
    tran0.writeAction("slorii X17 X17 12 1016")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
