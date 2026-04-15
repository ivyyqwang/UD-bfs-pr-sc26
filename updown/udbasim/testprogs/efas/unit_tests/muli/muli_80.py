from EFA_v2 import *
def muli_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1175025761875273818, 6475]
    tran0.writeAction("movir X16 61361")
    tran0.writeAction("slorii X16 X16 12 1924")
    tran0.writeAction("slorii X16 X16 12 2957")
    tran0.writeAction("slorii X16 X16 12 2013")
    tran0.writeAction("slorii X16 X16 12 1958")
    tran0.writeAction("muli X16 X17 6475")
    tran0.writeAction("yieldt")
    return efa
