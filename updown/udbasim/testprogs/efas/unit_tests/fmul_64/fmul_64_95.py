from EFA_v2 import *
def fmul_64_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7345471709119835461, 18288050924675604006]
    tran0.writeAction("movir X16 26096")
    tran0.writeAction("slorii X16 X16 12 1465")
    tran0.writeAction("slorii X16 X16 12 2553")
    tran0.writeAction("slorii X16 X16 12 3150")
    tran0.writeAction("slorii X16 X16 12 3397")
    tran0.writeAction("movir X17 64972")
    tran0.writeAction("slorii X17 X17 12 854")
    tran0.writeAction("slorii X17 X17 12 3063")
    tran0.writeAction("slorii X17 X17 12 2225")
    tran0.writeAction("slorii X17 X17 12 3622")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
