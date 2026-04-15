from EFA_v2 import *
def sladdii_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2219198348077211939, 0, 1244]
    tran0.writeAction("movir X16 7884")
    tran0.writeAction("slorii X16 X16 12 722")
    tran0.writeAction("slorii X16 X16 12 967")
    tran0.writeAction("slorii X16 X16 12 1130")
    tran0.writeAction("slorii X16 X16 12 291")
    tran0.writeAction("sladdii X16 X17 0 1244")
    tran0.writeAction("yieldt")
    return efa
