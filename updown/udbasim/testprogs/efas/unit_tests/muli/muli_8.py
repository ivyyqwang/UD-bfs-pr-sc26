from EFA_v2 import *
def muli_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3240988013386180477, 27255]
    tran0.writeAction("movir X16 11514")
    tran0.writeAction("slorii X16 X16 12 1238")
    tran0.writeAction("slorii X16 X16 12 3387")
    tran0.writeAction("slorii X16 X16 12 746")
    tran0.writeAction("slorii X16 X16 12 1917")
    tran0.writeAction("muli X16 X17 27255")
    tran0.writeAction("yieldt")
    return efa
