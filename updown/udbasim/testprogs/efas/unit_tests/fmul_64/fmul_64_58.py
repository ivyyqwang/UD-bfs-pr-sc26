from EFA_v2 import *
def fmul_64_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14257519986117555088, 1258643806943918731]
    tran0.writeAction("movir X16 50652")
    tran0.writeAction("slorii X16 X16 12 3630")
    tran0.writeAction("slorii X16 X16 12 838")
    tran0.writeAction("slorii X16 X16 12 2331")
    tran0.writeAction("slorii X16 X16 12 912")
    tran0.writeAction("movir X17 4471")
    tran0.writeAction("slorii X17 X17 12 2461")
    tran0.writeAction("slorii X17 X17 12 4019")
    tran0.writeAction("slorii X17 X17 12 2611")
    tran0.writeAction("slorii X17 X17 12 2699")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
