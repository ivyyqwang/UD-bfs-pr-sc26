from EFA_v2 import *
def fmul_64_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6361439000398336430, 5374520392652572423]
    tran0.writeAction("movir X16 22600")
    tran0.writeAction("slorii X16 X16 12 1521")
    tran0.writeAction("slorii X16 X16 12 263")
    tran0.writeAction("slorii X16 X16 12 241")
    tran0.writeAction("slorii X16 X16 12 430")
    tran0.writeAction("movir X17 19094")
    tran0.writeAction("slorii X17 X17 12 541")
    tran0.writeAction("slorii X17 X17 12 602")
    tran0.writeAction("slorii X17 X17 12 612")
    tran0.writeAction("slorii X17 X17 12 1799")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
