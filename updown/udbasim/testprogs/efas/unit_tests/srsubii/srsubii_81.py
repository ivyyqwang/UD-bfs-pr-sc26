from EFA_v2 import *
def srsubii_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6180381790249747648, 11, 1957]
    tran0.writeAction("movir X16 43578")
    tran0.writeAction("slorii X16 X16 12 3576")
    tran0.writeAction("slorii X16 X16 12 447")
    tran0.writeAction("slorii X16 X16 12 3567")
    tran0.writeAction("slorii X16 X16 12 2880")
    tran0.writeAction("srsubii X16 X17 11 1957")
    tran0.writeAction("yieldt")
    return efa
