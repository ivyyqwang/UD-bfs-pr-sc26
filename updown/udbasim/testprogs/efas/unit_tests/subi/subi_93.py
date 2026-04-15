from EFA_v2 import *
def subi_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4838560273629802705, -14416]
    tran0.writeAction("movir X16 17190")
    tran0.writeAction("slorii X16 X16 12 78")
    tran0.writeAction("slorii X16 X16 12 3806")
    tran0.writeAction("slorii X16 X16 12 87")
    tran0.writeAction("slorii X16 X16 12 209")
    tran0.writeAction("subi X16 X17 -14416")
    tran0.writeAction("yieldt")
    return efa
