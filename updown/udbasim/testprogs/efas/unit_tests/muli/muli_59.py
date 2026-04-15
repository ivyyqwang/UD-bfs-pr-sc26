from EFA_v2 import *
def muli_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6640590936940841448, 26375]
    tran0.writeAction("movir X16 23592")
    tran0.writeAction("slorii X16 X16 12 484")
    tran0.writeAction("slorii X16 X16 12 1559")
    tran0.writeAction("slorii X16 X16 12 152")
    tran0.writeAction("slorii X16 X16 12 2536")
    tran0.writeAction("muli X16 X17 26375")
    tran0.writeAction("yieldt")
    return efa
