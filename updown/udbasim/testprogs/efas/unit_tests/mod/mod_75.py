from EFA_v2 import *
def mod_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1748120536841614643, -2296727146482618808]
    tran0.writeAction("movir X16 59325")
    tran0.writeAction("slorii X16 X16 12 1754")
    tran0.writeAction("slorii X16 X16 12 568")
    tran0.writeAction("slorii X16 X16 12 4056")
    tran0.writeAction("slorii X16 X16 12 2765")
    tran0.writeAction("movir X17 57376")
    tran0.writeAction("slorii X17 X17 12 1581")
    tran0.writeAction("slorii X17 X17 12 1071")
    tran0.writeAction("slorii X17 X17 12 3714")
    tran0.writeAction("slorii X17 X17 12 3656")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
