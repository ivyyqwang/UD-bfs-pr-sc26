from EFA_v2 import *
def sladdii_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6423559427150334828, 3, 710]
    tran0.writeAction("movir X16 22821")
    tran0.writeAction("slorii X16 X16 12 276")
    tran0.writeAction("slorii X16 X16 12 1016")
    tran0.writeAction("slorii X16 X16 12 3716")
    tran0.writeAction("slorii X16 X16 12 2924")
    tran0.writeAction("sladdii X16 X17 3 710")
    tran0.writeAction("yieldt")
    return efa
