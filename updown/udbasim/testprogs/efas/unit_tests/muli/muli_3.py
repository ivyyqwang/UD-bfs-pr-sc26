from EFA_v2 import *
def muli_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6170458533528522877, 11503]
    tran0.writeAction("movir X16 43614")
    tran0.writeAction("slorii X16 X16 12 522")
    tran0.writeAction("slorii X16 X16 12 2047")
    tran0.writeAction("slorii X16 X16 12 3090")
    tran0.writeAction("slorii X16 X16 12 3971")
    tran0.writeAction("muli X16 X17 11503")
    tran0.writeAction("yieldt")
    return efa
