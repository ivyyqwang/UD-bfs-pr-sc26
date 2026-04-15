from EFA_v2 import *
def subi_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4958397779797068900, 26011]
    tran0.writeAction("movir X16 17615")
    tran0.writeAction("slorii X16 X16 12 3144")
    tran0.writeAction("slorii X16 X16 12 655")
    tran0.writeAction("slorii X16 X16 12 3644")
    tran0.writeAction("slorii X16 X16 12 3172")
    tran0.writeAction("subi X16 X17 26011")
    tran0.writeAction("yieldt")
    return efa
