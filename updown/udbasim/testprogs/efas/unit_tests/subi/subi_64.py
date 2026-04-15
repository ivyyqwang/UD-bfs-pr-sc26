from EFA_v2 import *
def subi_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7122496918176205847, 16888]
    tran0.writeAction("movir X16 25304")
    tran0.writeAction("slorii X16 X16 12 787")
    tran0.writeAction("slorii X16 X16 12 1505")
    tran0.writeAction("slorii X16 X16 12 2896")
    tran0.writeAction("slorii X16 X16 12 3095")
    tran0.writeAction("subi X16 X17 16888")
    tran0.writeAction("yieldt")
    return efa
