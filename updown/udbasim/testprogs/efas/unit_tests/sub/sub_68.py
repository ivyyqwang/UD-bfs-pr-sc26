from EFA_v2 import *
def sub_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4741545516134103534, -1071333583316166389]
    tran0.writeAction("movir X16 48690")
    tran0.writeAction("slorii X16 X16 12 2647")
    tran0.writeAction("slorii X16 X16 12 2448")
    tran0.writeAction("slorii X16 X16 12 1968")
    tran0.writeAction("slorii X16 X16 12 1554")
    tran0.writeAction("movir X17 61729")
    tran0.writeAction("slorii X17 X17 12 3516")
    tran0.writeAction("slorii X17 X17 12 2106")
    tran0.writeAction("slorii X17 X17 12 2021")
    tran0.writeAction("slorii X17 X17 12 2315")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
