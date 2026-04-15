from EFA_v2 import *
def slsubii_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2734161139599860977, 3, 1975]
    tran0.writeAction("movir X16 9713")
    tran0.writeAction("slorii X16 X16 12 2833")
    tran0.writeAction("slorii X16 X16 12 508")
    tran0.writeAction("slorii X16 X16 12 2158")
    tran0.writeAction("slorii X16 X16 12 1265")
    tran0.writeAction("slsubii X16 X17 3 1975")
    tran0.writeAction("yieldt")
    return efa
