from EFA_v2 import *
def slsubii_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [374533122348192942, 12, 1041]
    tran0.writeAction("movir X16 1330")
    tran0.writeAction("slorii X16 X16 12 2494")
    tran0.writeAction("slorii X16 X16 12 1010")
    tran0.writeAction("slorii X16 X16 12 745")
    tran0.writeAction("slorii X16 X16 12 1198")
    tran0.writeAction("slsubii X16 X17 12 1041")
    tran0.writeAction("yieldt")
    return efa
