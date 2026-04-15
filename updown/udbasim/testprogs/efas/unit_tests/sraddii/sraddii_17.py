from EFA_v2 import *
def sraddii_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5735294440574272015, 5, 331]
    tran0.writeAction("movir X16 20375")
    tran0.writeAction("slorii X16 X16 12 3518")
    tran0.writeAction("slorii X16 X16 12 2084")
    tran0.writeAction("slorii X16 X16 12 2876")
    tran0.writeAction("slorii X16 X16 12 527")
    tran0.writeAction("sraddii X16 X17 5 331")
    tran0.writeAction("yieldt")
    return efa
