from EFA_v2 import *
def sub_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8407440317520825481, 5871475847142212950]
    tran0.writeAction("movir X16 29869")
    tran0.writeAction("slorii X16 X16 12 934")
    tran0.writeAction("slorii X16 X16 12 3228")
    tran0.writeAction("slorii X16 X16 12 516")
    tran0.writeAction("slorii X16 X16 12 3209")
    tran0.writeAction("movir X17 20859")
    tran0.writeAction("slorii X17 X17 12 2754")
    tran0.writeAction("slorii X17 X17 12 3248")
    tran0.writeAction("slorii X17 X17 12 808")
    tran0.writeAction("slorii X17 X17 12 1366")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
