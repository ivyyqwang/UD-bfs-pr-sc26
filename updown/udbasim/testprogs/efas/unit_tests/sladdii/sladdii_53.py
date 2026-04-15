from EFA_v2 import *
def sladdii_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2142733036057406889, 4, 942]
    tran0.writeAction("movir X16 7612")
    tran0.writeAction("slorii X16 X16 12 2117")
    tran0.writeAction("slorii X16 X16 12 2038")
    tran0.writeAction("slorii X16 X16 12 2850")
    tran0.writeAction("slorii X16 X16 12 3497")
    tran0.writeAction("sladdii X16 X17 4 942")
    tran0.writeAction("yieldt")
    return efa
