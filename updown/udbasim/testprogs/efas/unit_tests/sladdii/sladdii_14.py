from EFA_v2 import *
def sladdii_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4222838427762181983, 13, 271]
    tran0.writeAction("movir X16 15002")
    tran0.writeAction("slorii X16 X16 12 2194")
    tran0.writeAction("slorii X16 X16 12 3374")
    tran0.writeAction("slorii X16 X16 12 2596")
    tran0.writeAction("slorii X16 X16 12 1887")
    tran0.writeAction("sladdii X16 X17 13 271")
    tran0.writeAction("yieldt")
    return efa
