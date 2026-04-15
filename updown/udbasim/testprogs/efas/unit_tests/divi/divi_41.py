from EFA_v2 import *
def divi_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3509652804256592152, -22127]
    tran0.writeAction("movir X16 53067")
    tran0.writeAction("slorii X16 X16 12 853")
    tran0.writeAction("slorii X16 X16 12 3733")
    tran0.writeAction("slorii X16 X16 12 1360")
    tran0.writeAction("slorii X16 X16 12 3816")
    tran0.writeAction("divi X16 X17 -22127")
    tran0.writeAction("yieldt")
    return efa
