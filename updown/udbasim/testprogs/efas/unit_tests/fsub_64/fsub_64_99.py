from EFA_v2 import *
def fsub_64_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12192857112034582731, 3281464893088107086]
    tran0.writeAction("movir X16 43317")
    tran0.writeAction("slorii X16 X16 12 2991")
    tran0.writeAction("slorii X16 X16 12 351")
    tran0.writeAction("slorii X16 X16 12 3754")
    tran0.writeAction("slorii X16 X16 12 203")
    tran0.writeAction("movir X17 11658")
    tran0.writeAction("slorii X17 X17 12 430")
    tran0.writeAction("slorii X17 X17 12 3887")
    tran0.writeAction("slorii X17 X17 12 1768")
    tran0.writeAction("slorii X17 X17 12 2638")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
