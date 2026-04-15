from EFA_v2 import *
def sraddii_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4981099613676688692, 14, 1908]
    tran0.writeAction("movir X16 47839")
    tran0.writeAction("slorii X16 X16 12 2372")
    tran0.writeAction("slorii X16 X16 12 2775")
    tran0.writeAction("slorii X16 X16 12 3954")
    tran0.writeAction("slorii X16 X16 12 2764")
    tran0.writeAction("sraddii X16 X17 14 1908")
    tran0.writeAction("yieldt")
    return efa
