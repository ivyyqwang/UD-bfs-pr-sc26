from EFA_v2 import *
def mod_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6682899293883853432, 8618844433812615438]
    tran0.writeAction("movir X16 23742")
    tran0.writeAction("slorii X16 X16 12 1752")
    tran0.writeAction("slorii X16 X16 12 17")
    tran0.writeAction("slorii X16 X16 12 2686")
    tran0.writeAction("slorii X16 X16 12 2680")
    tran0.writeAction("movir X17 30620")
    tran0.writeAction("slorii X17 X17 12 1173")
    tran0.writeAction("slorii X17 X17 12 2323")
    tran0.writeAction("slorii X17 X17 12 3087")
    tran0.writeAction("slorii X17 X17 12 270")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
