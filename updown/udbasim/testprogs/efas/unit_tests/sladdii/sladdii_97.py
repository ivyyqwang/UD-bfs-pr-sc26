from EFA_v2 import *
def sladdii_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3349118860318937101, 9, 509]
    tran0.writeAction("movir X16 53637")
    tran0.writeAction("slorii X16 X16 12 2210")
    tran0.writeAction("slorii X16 X16 12 1044")
    tran0.writeAction("slorii X16 X16 12 526")
    tran0.writeAction("slorii X16 X16 12 4083")
    tran0.writeAction("sladdii X16 X17 9 509")
    tran0.writeAction("yieldt")
    return efa
