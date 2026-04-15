from EFA_v2 import *
def fmul_64_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [919134862370298263, 17992281178533571805]
    tran0.writeAction("movir X16 3265")
    tran0.writeAction("slorii X16 X16 12 1732")
    tran0.writeAction("slorii X16 X16 12 2460")
    tran0.writeAction("slorii X16 X16 12 1061")
    tran0.writeAction("slorii X16 X16 12 2455")
    tran0.writeAction("movir X17 63921")
    tran0.writeAction("slorii X17 X17 12 1734")
    tran0.writeAction("slorii X17 X17 12 1945")
    tran0.writeAction("slorii X17 X17 12 1802")
    tran0.writeAction("slorii X17 X17 12 3293")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
