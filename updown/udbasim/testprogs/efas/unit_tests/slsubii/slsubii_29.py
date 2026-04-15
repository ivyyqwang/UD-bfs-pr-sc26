from EFA_v2 import *
def slsubii_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5350776995314147956, 12, 885]
    tran0.writeAction("movir X16 19009")
    tran0.writeAction("slorii X16 X16 12 3189")
    tran0.writeAction("slorii X16 X16 12 990")
    tran0.writeAction("slorii X16 X16 12 130")
    tran0.writeAction("slorii X16 X16 12 628")
    tran0.writeAction("slsubii X16 X17 12 885")
    tran0.writeAction("yieldt")
    return efa
