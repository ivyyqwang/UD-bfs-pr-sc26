from EFA_v2 import *
def sladdii_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4145159424017712615, 12, 11]
    tran0.writeAction("movir X16 50809")
    tran0.writeAction("slorii X16 X16 12 1783")
    tran0.writeAction("slorii X16 X16 12 1858")
    tran0.writeAction("slorii X16 X16 12 251")
    tran0.writeAction("slorii X16 X16 12 2585")
    tran0.writeAction("sladdii X16 X17 12 11")
    tran0.writeAction("yieldt")
    return efa
