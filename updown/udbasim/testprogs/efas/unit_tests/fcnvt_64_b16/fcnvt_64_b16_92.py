from EFA_v2 import *
def fcnvt_64_b16_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12570300483702903548]
    tran0.writeAction("movir X16 44658")
    tran0.writeAction("slorii X16 X16 12 2779")
    tran0.writeAction("slorii X16 X16 12 139")
    tran0.writeAction("slorii X16 X16 12 133")
    tran0.writeAction("slorii X16 X16 12 764")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
