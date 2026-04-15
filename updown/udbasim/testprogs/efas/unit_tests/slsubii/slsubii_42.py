from EFA_v2 import *
def slsubii_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7217077730139038167, 15, 651]
    tran0.writeAction("movir X16 39895")
    tran0.writeAction("slorii X16 X16 12 3232")
    tran0.writeAction("slorii X16 X16 12 2762")
    tran0.writeAction("slorii X16 X16 12 2785")
    tran0.writeAction("slorii X16 X16 12 3625")
    tran0.writeAction("slsubii X16 X17 15 651")
    tran0.writeAction("yieldt")
    return efa
