from EFA_v2 import *
def sraddii_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [300079235650838142, 8, 316]
    tran0.writeAction("movir X16 1066")
    tran0.writeAction("slorii X16 X16 12 391")
    tran0.writeAction("slorii X16 X16 12 2453")
    tran0.writeAction("slorii X16 X16 12 1797")
    tran0.writeAction("slorii X16 X16 12 3710")
    tran0.writeAction("sraddii X16 X17 8 316")
    tran0.writeAction("yieldt")
    return efa
