from EFA_v2 import *
def subi_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3267013120181874133, -22947]
    tran0.writeAction("movir X16 53929")
    tran0.writeAction("slorii X16 X16 12 974")
    tran0.writeAction("slorii X16 X16 12 103")
    tran0.writeAction("slorii X16 X16 12 77")
    tran0.writeAction("slorii X16 X16 12 555")
    tran0.writeAction("subi X16 X17 -22947")
    tran0.writeAction("yieldt")
    return efa
