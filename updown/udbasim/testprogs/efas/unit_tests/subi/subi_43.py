from EFA_v2 import *
def subi_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3734461119399298022, -25284]
    tran0.writeAction("movir X16 52268")
    tran0.writeAction("slorii X16 X16 12 2166")
    tran0.writeAction("slorii X16 X16 12 1502")
    tran0.writeAction("slorii X16 X16 12 2855")
    tran0.writeAction("slorii X16 X16 12 3098")
    tran0.writeAction("subi X16 X17 -25284")
    tran0.writeAction("yieldt")
    return efa
