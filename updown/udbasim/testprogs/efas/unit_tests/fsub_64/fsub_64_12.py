from EFA_v2 import *
def fsub_64_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15299442253385934683, 12614978166055690177]
    tran0.writeAction("movir X16 54354")
    tran0.writeAction("slorii X16 X16 12 2202")
    tran0.writeAction("slorii X16 X16 12 2918")
    tran0.writeAction("slorii X16 X16 12 2746")
    tran0.writeAction("slorii X16 X16 12 1883")
    tran0.writeAction("movir X17 44817")
    tran0.writeAction("slorii X17 X17 12 1660")
    tran0.writeAction("slorii X17 X17 12 3605")
    tran0.writeAction("slorii X17 X17 12 237")
    tran0.writeAction("slorii X17 X17 12 4033")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
