from EFA_v2 import *
def mul_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [421698335539426727, 8907070707320939431]
    tran0.writeAction("movir X16 1498")
    tran0.writeAction("slorii X16 X16 12 710")
    tran0.writeAction("slorii X16 X16 12 1764")
    tran0.writeAction("slorii X16 X16 12 823")
    tran0.writeAction("slorii X16 X16 12 1447")
    tran0.writeAction("movir X17 31644")
    tran0.writeAction("slorii X17 X17 12 1113")
    tran0.writeAction("slorii X17 X17 12 3547")
    tran0.writeAction("slorii X17 X17 12 622")
    tran0.writeAction("slorii X17 X17 12 935")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
