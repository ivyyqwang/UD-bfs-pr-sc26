from EFA_v2 import *
def muli_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4168154348547981857, 13556]
    tran0.writeAction("movir X16 50727")
    tran0.writeAction("slorii X16 X16 12 3035")
    tran0.writeAction("slorii X16 X16 12 1069")
    tran0.writeAction("slorii X16 X16 12 3267")
    tran0.writeAction("slorii X16 X16 12 3551")
    tran0.writeAction("muli X16 X17 13556")
    tran0.writeAction("yieldt")
    return efa
