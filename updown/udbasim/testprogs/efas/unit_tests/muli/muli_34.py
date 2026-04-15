from EFA_v2 import *
def muli_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5348351262223802575, 8533]
    tran0.writeAction("movir X16 46534")
    tran0.writeAction("slorii X16 X16 12 3437")
    tran0.writeAction("slorii X16 X16 12 3361")
    tran0.writeAction("slorii X16 X16 12 565")
    tran0.writeAction("slorii X16 X16 12 3889")
    tran0.writeAction("muli X16 X17 8533")
    tran0.writeAction("yieldt")
    return efa
