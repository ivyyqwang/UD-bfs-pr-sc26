from EFA_v2 import *
def modi_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3419802790604823773, 12233]
    tran0.writeAction("movir X16 53386")
    tran0.writeAction("slorii X16 X16 12 1719")
    tran0.writeAction("slorii X16 X16 12 2840")
    tran0.writeAction("slorii X16 X16 12 450")
    tran0.writeAction("slorii X16 X16 12 803")
    tran0.writeAction("modi X16 X17 12233")
    tran0.writeAction("yieldt")
    return efa
