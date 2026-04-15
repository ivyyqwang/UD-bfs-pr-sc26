from EFA_v2 import *
def srsubii_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3503757154055400272, 3, 316]
    tran0.writeAction("movir X16 12447")
    tran0.writeAction("slorii X16 X16 12 3465")
    tran0.writeAction("slorii X16 X16 12 354")
    tran0.writeAction("slorii X16 X16 12 2890")
    tran0.writeAction("slorii X16 X16 12 2896")
    tran0.writeAction("srsubii X16 X17 3 316")
    tran0.writeAction("yieldt")
    return efa
