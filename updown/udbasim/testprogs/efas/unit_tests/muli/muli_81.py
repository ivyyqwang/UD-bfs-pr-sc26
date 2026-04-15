from EFA_v2 import *
def muli_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3230962778767182572, -3944]
    tran0.writeAction("movir X16 54057")
    tran0.writeAction("slorii X16 X16 12 1287")
    tran0.writeAction("slorii X16 X16 12 2201")
    tran0.writeAction("slorii X16 X16 12 299")
    tran0.writeAction("slorii X16 X16 12 1300")
    tran0.writeAction("muli X16 X17 -3944")
    tran0.writeAction("yieldt")
    return efa
