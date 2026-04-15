from EFA_v2 import *
def sladdii_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5815492701028178135, 13, 1427]
    tran0.writeAction("movir X16 44875")
    tran0.writeAction("slorii X16 X16 12 899")
    tran0.writeAction("slorii X16 X16 12 833")
    tran0.writeAction("slorii X16 X16 12 1386")
    tran0.writeAction("slorii X16 X16 12 1833")
    tran0.writeAction("sladdii X16 X17 13 1427")
    tran0.writeAction("yieldt")
    return efa
