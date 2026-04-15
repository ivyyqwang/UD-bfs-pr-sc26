from EFA_v2 import *
def muli_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2879989681680150441, 30693]
    tran0.writeAction("movir X16 10231")
    tran0.writeAction("slorii X16 X16 12 3189")
    tran0.writeAction("slorii X16 X16 12 2893")
    tran0.writeAction("slorii X16 X16 12 1374")
    tran0.writeAction("slorii X16 X16 12 4009")
    tran0.writeAction("muli X16 X17 30693")
    tran0.writeAction("yieldt")
    return efa
