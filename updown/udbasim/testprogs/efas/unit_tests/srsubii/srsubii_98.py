from EFA_v2 import *
def srsubii_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5587862147597248878, 9, 589]
    tran0.writeAction("movir X16 19852")
    tran0.writeAction("slorii X16 X16 12 304")
    tran0.writeAction("slorii X16 X16 12 1145")
    tran0.writeAction("slorii X16 X16 12 1578")
    tran0.writeAction("slorii X16 X16 12 2414")
    tran0.writeAction("srsubii X16 X17 9 589")
    tran0.writeAction("yieldt")
    return efa
