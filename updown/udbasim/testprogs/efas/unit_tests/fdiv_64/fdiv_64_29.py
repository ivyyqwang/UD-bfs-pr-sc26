from EFA_v2 import *
def fdiv_64_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17474573868379598417, 10449660072813162836]
    tran0.writeAction("movir X16 62082")
    tran0.writeAction("slorii X16 X16 12 645")
    tran0.writeAction("slorii X16 X16 12 2394")
    tran0.writeAction("slorii X16 X16 12 366")
    tran0.writeAction("slorii X16 X16 12 3665")
    tran0.writeAction("movir X17 37124")
    tran0.writeAction("slorii X17 X17 12 2663")
    tran0.writeAction("slorii X17 X17 12 2231")
    tran0.writeAction("slorii X17 X17 12 2503")
    tran0.writeAction("slorii X17 X17 12 340")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
