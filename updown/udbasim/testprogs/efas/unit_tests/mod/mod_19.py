from EFA_v2 import *
def mod_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8126562175680815156, -6506726305873394788]
    tran0.writeAction("movir X16 36664")
    tran0.writeAction("slorii X16 X16 12 2668")
    tran0.writeAction("slorii X16 X16 12 497")
    tran0.writeAction("slorii X16 X16 12 1717")
    tran0.writeAction("slorii X16 X16 12 4044")
    tran0.writeAction("movir X17 42419")
    tran0.writeAction("slorii X17 X17 12 1902")
    tran0.writeAction("slorii X17 X17 12 1567")
    tran0.writeAction("slorii X17 X17 12 2976")
    tran0.writeAction("slorii X17 X17 12 924")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
