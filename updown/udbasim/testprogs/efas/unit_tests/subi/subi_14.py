from EFA_v2 import *
def subi_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7589246350437376617, -15355]
    tran0.writeAction("movir X16 38573")
    tran0.writeAction("slorii X16 X16 12 2378")
    tran0.writeAction("slorii X16 X16 12 1889")
    tran0.writeAction("slorii X16 X16 12 1025")
    tran0.writeAction("slorii X16 X16 12 3479")
    tran0.writeAction("subi X16 X17 -15355")
    tran0.writeAction("yieldt")
    return efa
