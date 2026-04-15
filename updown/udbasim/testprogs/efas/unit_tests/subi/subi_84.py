from EFA_v2 import *
def subi_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-292980567408084622, 31645]
    tran0.writeAction("movir X16 64495")
    tran0.writeAction("slorii X16 X16 12 507")
    tran0.writeAction("slorii X16 X16 12 2537")
    tran0.writeAction("slorii X16 X16 12 2247")
    tran0.writeAction("slorii X16 X16 12 2418")
    tran0.writeAction("subi X16 X17 31645")
    tran0.writeAction("yieldt")
    return efa
