from EFA_v2 import *
def sraddii_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7218916047871879758, 4, 907]
    tran0.writeAction("movir X16 25646")
    tran0.writeAction("slorii X16 X16 12 3038")
    tran0.writeAction("slorii X16 X16 12 1512")
    tran0.writeAction("slorii X16 X16 12 3154")
    tran0.writeAction("slorii X16 X16 12 2638")
    tran0.writeAction("sraddii X16 X17 4 907")
    tran0.writeAction("yieldt")
    return efa
