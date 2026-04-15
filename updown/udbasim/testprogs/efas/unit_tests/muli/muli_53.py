from EFA_v2 import *
def muli_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7740200659482934882, -9612]
    tran0.writeAction("movir X16 27498")
    tran0.writeAction("slorii X16 X16 12 2935")
    tran0.writeAction("slorii X16 X16 12 3470")
    tran0.writeAction("slorii X16 X16 12 2967")
    tran0.writeAction("slorii X16 X16 12 3682")
    tran0.writeAction("muli X16 X17 -9612")
    tran0.writeAction("yieldt")
    return efa
