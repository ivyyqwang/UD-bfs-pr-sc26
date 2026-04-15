from EFA_v2 import *
def fmul_64_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5265077230099947793, 4075659506200094605]
    tran0.writeAction("movir X16 18705")
    tran0.writeAction("slorii X16 X16 12 1277")
    tran0.writeAction("slorii X16 X16 12 2143")
    tran0.writeAction("slorii X16 X16 12 430")
    tran0.writeAction("slorii X16 X16 12 273")
    tran0.writeAction("movir X17 14479")
    tran0.writeAction("slorii X17 X17 12 2667")
    tran0.writeAction("slorii X17 X17 12 2596")
    tran0.writeAction("slorii X17 X17 12 2050")
    tran0.writeAction("slorii X17 X17 12 1933")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
