from EFA_v2 import *
def sladdii_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7744083917182759032, 9, 726]
    tran0.writeAction("movir X16 27512")
    tran0.writeAction("slorii X16 X16 12 2100")
    tran0.writeAction("slorii X16 X16 12 2802")
    tran0.writeAction("slorii X16 X16 12 2023")
    tran0.writeAction("slorii X16 X16 12 120")
    tran0.writeAction("sladdii X16 X17 9 726")
    tran0.writeAction("yieldt")
    return efa
