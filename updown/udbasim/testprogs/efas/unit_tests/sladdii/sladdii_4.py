from EFA_v2 import *
def sladdii_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [219814897530647333, 11, 1266]
    tran0.writeAction("movir X16 780")
    tran0.writeAction("slorii X16 X16 12 3847")
    tran0.writeAction("slorii X16 X16 12 3091")
    tran0.writeAction("slorii X16 X16 12 2675")
    tran0.writeAction("slorii X16 X16 12 805")
    tran0.writeAction("sladdii X16 X17 11 1266")
    tran0.writeAction("yieldt")
    return efa
