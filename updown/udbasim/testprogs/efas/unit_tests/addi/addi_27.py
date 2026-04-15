from EFA_v2 import *
def addi_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [690123481967538317, -29178]
    tran0.writeAction("movir X16 2451")
    tran0.writeAction("slorii X16 X16 12 3322")
    tran0.writeAction("slorii X16 X16 12 1665")
    tran0.writeAction("slorii X16 X16 12 3403")
    tran0.writeAction("slorii X16 X16 12 141")
    tran0.writeAction("addi X16 X17 -29178")
    tran0.writeAction("yieldt")
    return efa
