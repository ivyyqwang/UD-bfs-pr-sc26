from EFA_v2 import *
def muli_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4854883483094566737, 24321]
    tran0.writeAction("movir X16 48287")
    tran0.writeAction("slorii X16 X16 12 4051")
    tran0.writeAction("slorii X16 X16 12 452")
    tran0.writeAction("slorii X16 X16 12 971")
    tran0.writeAction("slorii X16 X16 12 2223")
    tran0.writeAction("muli X16 X17 24321")
    tran0.writeAction("yieldt")
    return efa
