from EFA_v2 import *
def fmul_64_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7080752444548109134, 8429127786021423821]
    tran0.writeAction("movir X16 25155")
    tran0.writeAction("slorii X16 X16 12 3629")
    tran0.writeAction("slorii X16 X16 12 1335")
    tran0.writeAction("slorii X16 X16 12 3149")
    tran0.writeAction("slorii X16 X16 12 846")
    tran0.writeAction("movir X17 29946")
    tran0.writeAction("slorii X17 X17 12 1136")
    tran0.writeAction("slorii X17 X17 12 4060")
    tran0.writeAction("slorii X17 X17 12 744")
    tran0.writeAction("slorii X17 X17 12 2765")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
