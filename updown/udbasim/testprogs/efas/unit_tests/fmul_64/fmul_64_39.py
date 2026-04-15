from EFA_v2 import *
def fmul_64_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18296704448415765864, 8825193766275709594]
    tran0.writeAction("movir X16 65002")
    tran0.writeAction("slorii X16 X16 12 3900")
    tran0.writeAction("slorii X16 X16 12 376")
    tran0.writeAction("slorii X16 X16 12 537")
    tran0.writeAction("slorii X16 X16 12 1384")
    tran0.writeAction("movir X17 31353")
    tran0.writeAction("slorii X17 X17 12 1583")
    tran0.writeAction("slorii X17 X17 12 2296")
    tran0.writeAction("slorii X17 X17 12 3503")
    tran0.writeAction("slorii X17 X17 12 2714")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
