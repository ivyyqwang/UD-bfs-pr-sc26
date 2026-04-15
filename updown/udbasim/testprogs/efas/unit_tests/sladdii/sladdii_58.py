from EFA_v2 import *
def sladdii_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [130970718180168270, 15, 1698]
    tran0.writeAction("movir X16 465")
    tran0.writeAction("slorii X16 X16 12 1234")
    tran0.writeAction("slorii X16 X16 12 3229")
    tran0.writeAction("slorii X16 X16 12 437")
    tran0.writeAction("slorii X16 X16 12 590")
    tran0.writeAction("sladdii X16 X17 15 1698")
    tran0.writeAction("yieldt")
    return efa
