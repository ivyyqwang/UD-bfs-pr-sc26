from EFA_v2 import *
def hash_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8009235648129869995, -344962048006297789]
    tran0.writeAction("movir X16 37081")
    tran0.writeAction("slorii X16 X16 12 1961")
    tran0.writeAction("slorii X16 X16 12 3294")
    tran0.writeAction("slorii X16 X16 12 3373")
    tran0.writeAction("slorii X16 X16 12 1877")
    tran0.writeAction("movir X17 64310")
    tran0.writeAction("slorii X17 X17 12 1837")
    tran0.writeAction("slorii X17 X17 12 2131")
    tran0.writeAction("slorii X17 X17 12 2430")
    tran0.writeAction("slorii X17 X17 12 1859")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
