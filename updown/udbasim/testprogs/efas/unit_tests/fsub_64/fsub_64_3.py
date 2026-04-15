from EFA_v2 import *
def fsub_64_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17347348305691433730, 9573997289503476261]
    tran0.writeAction("movir X16 61630")
    tran0.writeAction("slorii X16 X16 12 661")
    tran0.writeAction("slorii X16 X16 12 4019")
    tran0.writeAction("slorii X16 X16 12 2917")
    tran0.writeAction("slorii X16 X16 12 2818")
    tran0.writeAction("movir X17 34013")
    tran0.writeAction("slorii X17 X17 12 2748")
    tran0.writeAction("slorii X17 X17 12 3905")
    tran0.writeAction("slorii X17 X17 12 1668")
    tran0.writeAction("slorii X17 X17 12 2597")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
