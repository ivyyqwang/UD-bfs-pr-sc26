from EFA_v2 import *
def sub_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3754364476604264346, 3877500965140551814]
    tran0.writeAction("movir X16 52197")
    tran0.writeAction("slorii X16 X16 12 3350")
    tran0.writeAction("slorii X16 X16 12 1638")
    tran0.writeAction("slorii X16 X16 12 2693")
    tran0.writeAction("slorii X16 X16 12 102")
    tran0.writeAction("movir X17 13775")
    tran0.writeAction("slorii X17 X17 12 2665")
    tran0.writeAction("slorii X17 X17 12 1403")
    tran0.writeAction("slorii X17 X17 12 1789")
    tran0.writeAction("slorii X17 X17 12 2182")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
