from EFA_v2 import *
def muli_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4642714216202700381, 2228]
    tran0.writeAction("movir X16 16494")
    tran0.writeAction("slorii X16 X16 12 959")
    tran0.writeAction("slorii X16 X16 12 2882")
    tran0.writeAction("slorii X16 X16 12 1712")
    tran0.writeAction("slorii X16 X16 12 1629")
    tran0.writeAction("muli X16 X17 2228")
    tran0.writeAction("yieldt")
    return efa
