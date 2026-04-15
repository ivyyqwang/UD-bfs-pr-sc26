from EFA_v2 import *
def sladdii_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3054641317080216408, 11, 1780]
    tran0.writeAction("movir X16 54683")
    tran0.writeAction("slorii X16 X16 12 3006")
    tran0.writeAction("slorii X16 X16 12 2051")
    tran0.writeAction("slorii X16 X16 12 828")
    tran0.writeAction("slorii X16 X16 12 3240")
    tran0.writeAction("sladdii X16 X17 11 1780")
    tran0.writeAction("yieldt")
    return efa
