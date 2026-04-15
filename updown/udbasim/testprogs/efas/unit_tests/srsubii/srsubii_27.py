from EFA_v2 import *
def srsubii_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3882282481475645544, 1, 1519]
    tran0.writeAction("movir X16 13792")
    tran0.writeAction("slorii X16 X16 12 2613")
    tran0.writeAction("slorii X16 X16 12 2306")
    tran0.writeAction("slorii X16 X16 12 319")
    tran0.writeAction("slorii X16 X16 12 104")
    tran0.writeAction("srsubii X16 X17 1 1519")
    tran0.writeAction("yieldt")
    return efa
