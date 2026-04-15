from EFA_v2 import *
def sladdii_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1731545040732476218, 15, 1329]
    tran0.writeAction("movir X16 6151")
    tran0.writeAction("slorii X16 X16 12 2800")
    tran0.writeAction("slorii X16 X16 12 2649")
    tran0.writeAction("slorii X16 X16 12 1837")
    tran0.writeAction("slorii X16 X16 12 826")
    tran0.writeAction("sladdii X16 X17 15 1329")
    tran0.writeAction("yieldt")
    return efa
