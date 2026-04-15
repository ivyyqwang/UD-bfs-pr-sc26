from EFA_v2 import *
def sladdii_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5149927934340924532, 15, 405]
    tran0.writeAction("movir X16 18296")
    tran0.writeAction("slorii X16 X16 12 898")
    tran0.writeAction("slorii X16 X16 12 3001")
    tran0.writeAction("slorii X16 X16 12 1032")
    tran0.writeAction("slorii X16 X16 12 1140")
    tran0.writeAction("sladdii X16 X17 15 405")
    tran0.writeAction("yieldt")
    return efa
