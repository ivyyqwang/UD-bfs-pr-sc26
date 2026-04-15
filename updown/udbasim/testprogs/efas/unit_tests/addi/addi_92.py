from EFA_v2 import *
def addi_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5918918495311354532, -14019]
    tran0.writeAction("movir X16 21028")
    tran0.writeAction("slorii X16 X16 12 912")
    tran0.writeAction("slorii X16 X16 12 767")
    tran0.writeAction("slorii X16 X16 12 2141")
    tran0.writeAction("slorii X16 X16 12 2724")
    tran0.writeAction("addi X16 X17 -14019")
    tran0.writeAction("yieldt")
    return efa
