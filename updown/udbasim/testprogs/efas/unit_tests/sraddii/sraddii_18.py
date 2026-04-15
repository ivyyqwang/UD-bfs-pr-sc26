from EFA_v2 import *
def sraddii_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3363602778184309021, 8, 1520]
    tran0.writeAction("movir X16 11949")
    tran0.writeAction("slorii X16 X16 12 3758")
    tran0.writeAction("slorii X16 X16 12 2007")
    tran0.writeAction("slorii X16 X16 12 789")
    tran0.writeAction("slorii X16 X16 12 2333")
    tran0.writeAction("sraddii X16 X17 8 1520")
    tran0.writeAction("yieldt")
    return efa
