from EFA_v2 import *
def fadd_64_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9380122145859652862, 2108133705494520203]
    tran0.writeAction("movir X16 33324")
    tran0.writeAction("slorii X16 X16 12 3638")
    tran0.writeAction("slorii X16 X16 12 1221")
    tran0.writeAction("slorii X16 X16 12 3028")
    tran0.writeAction("slorii X16 X16 12 3326")
    tran0.writeAction("movir X17 7489")
    tran0.writeAction("slorii X17 X17 12 2438")
    tran0.writeAction("slorii X17 X17 12 3983")
    tran0.writeAction("slorii X17 X17 12 118")
    tran0.writeAction("slorii X17 X17 12 395")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
