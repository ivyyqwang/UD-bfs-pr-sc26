from EFA_v2 import *
def sraddii_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3428674811989008691, 0, 638]
    tran0.writeAction("movir X16 53354")
    tran0.writeAction("slorii X16 X16 12 3686")
    tran0.writeAction("slorii X16 X16 12 3237")
    tran0.writeAction("slorii X16 X16 12 269")
    tran0.writeAction("slorii X16 X16 12 3789")
    tran0.writeAction("sraddii X16 X17 0 638")
    tran0.writeAction("yieldt")
    return efa
