from EFA_v2 import *
def add_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3460420676876194582, -3270002456717573289]
    tran0.writeAction("movir X16 12293")
    tran0.writeAction("slorii X16 X16 12 3620")
    tran0.writeAction("slorii X16 X16 12 1410")
    tran0.writeAction("slorii X16 X16 12 2549")
    tran0.writeAction("slorii X16 X16 12 790")
    tran0.writeAction("movir X17 53918")
    tran0.writeAction("slorii X17 X17 12 2529")
    tran0.writeAction("slorii X17 X17 12 1856")
    tran0.writeAction("slorii X17 X17 12 2844")
    tran0.writeAction("slorii X17 X17 12 855")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
