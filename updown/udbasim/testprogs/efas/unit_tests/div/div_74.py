from EFA_v2 import *
def div_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6728300218436132587, 3986549871015287953]
    tran0.writeAction("movir X16 41632")
    tran0.writeAction("slorii X16 X16 12 1129")
    tran0.writeAction("slorii X16 X16 12 2417")
    tran0.writeAction("slorii X16 X16 12 3814")
    tran0.writeAction("slorii X16 X16 12 277")
    tran0.writeAction("movir X17 14163")
    tran0.writeAction("slorii X17 X17 12 287")
    tran0.writeAction("slorii X17 X17 12 3181")
    tran0.writeAction("slorii X17 X17 12 1005")
    tran0.writeAction("slorii X17 X17 12 3217")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
