from EFA_v2 import *
def fsub_32_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4008423227, 2778262870]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 238")
    tran0.writeAction("slorii X16 X16 12 3770")
    tran0.writeAction("slorii X16 X16 12 3899")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 165")
    tran0.writeAction("slorii X17 X17 12 2446")
    tran0.writeAction("slorii X17 X17 12 3414")
    tran0.writeAction("fsub.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
