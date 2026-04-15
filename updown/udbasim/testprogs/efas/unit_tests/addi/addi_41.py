from EFA_v2 import *
def addi_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3998130284431368029, -30718]
    tran0.writeAction("movir X16 14204")
    tran0.writeAction("slorii X16 X16 12 868")
    tran0.writeAction("slorii X16 X16 12 3977")
    tran0.writeAction("slorii X16 X16 12 1077")
    tran0.writeAction("slorii X16 X16 12 3933")
    tran0.writeAction("addi X16 X17 -30718")
    tran0.writeAction("yieldt")
    return efa
