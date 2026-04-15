from EFA_v2 import *
def sladdii_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1047835346131220291, 14, 1775]
    tran0.writeAction("movir X16 61813")
    tran0.writeAction("slorii X16 X16 12 1396")
    tran0.writeAction("slorii X16 X16 12 3562")
    tran0.writeAction("slorii X16 X16 12 3072")
    tran0.writeAction("slorii X16 X16 12 2237")
    tran0.writeAction("sladdii X16 X17 14 1775")
    tran0.writeAction("yieldt")
    return efa
