from EFA_v2 import *
def mod_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4810680713852986972, -1120114721405041101]
    tran0.writeAction("movir X16 17090")
    tran0.writeAction("slorii X16 X16 12 3977")
    tran0.writeAction("slorii X16 X16 12 3845")
    tran0.writeAction("slorii X16 X16 12 122")
    tran0.writeAction("slorii X16 X16 12 1628")
    tran0.writeAction("movir X17 61556")
    tran0.writeAction("slorii X17 X17 12 2265")
    tran0.writeAction("slorii X17 X17 12 2162")
    tran0.writeAction("slorii X17 X17 12 3960")
    tran0.writeAction("slorii X17 X17 12 1587")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
