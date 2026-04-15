from EFA_v2 import *
def fsub_64_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3954132724686405450, 13308496634301874922]
    tran0.writeAction("movir X16 14047")
    tran0.writeAction("slorii X16 X16 12 3692")
    tran0.writeAction("slorii X16 X16 12 865")
    tran0.writeAction("slorii X16 X16 12 2787")
    tran0.writeAction("slorii X16 X16 12 3914")
    tran0.writeAction("movir X17 47281")
    tran0.writeAction("slorii X17 X17 12 1138")
    tran0.writeAction("slorii X17 X17 12 3438")
    tran0.writeAction("slorii X17 X17 12 184")
    tran0.writeAction("slorii X17 X17 12 746")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
