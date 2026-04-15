from EFA_v2 import *
def sladdii_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1691951135989857666, 9, 1707]
    tran0.writeAction("movir X16 6011")
    tran0.writeAction("slorii X16 X16 12 73")
    tran0.writeAction("slorii X16 X16 12 2053")
    tran0.writeAction("slorii X16 X16 12 4071")
    tran0.writeAction("slorii X16 X16 12 3458")
    tran0.writeAction("sladdii X16 X17 9 1707")
    tran0.writeAction("yieldt")
    return efa
