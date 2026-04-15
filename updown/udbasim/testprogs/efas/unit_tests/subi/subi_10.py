from EFA_v2 import *
def subi_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5852334010978176763, -10190]
    tran0.writeAction("movir X16 44744")
    tran0.writeAction("slorii X16 X16 12 1363")
    tran0.writeAction("slorii X16 X16 12 2392")
    tran0.writeAction("slorii X16 X16 12 2903")
    tran0.writeAction("slorii X16 X16 12 261")
    tran0.writeAction("subi X16 X17 -10190")
    tran0.writeAction("yieldt")
    return efa
