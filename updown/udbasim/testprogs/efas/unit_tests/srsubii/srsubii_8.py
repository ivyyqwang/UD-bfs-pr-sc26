from EFA_v2 import *
def srsubii_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6440503025945001421, 12, 147]
    tran0.writeAction("movir X16 22881")
    tran0.writeAction("slorii X16 X16 12 1078")
    tran0.writeAction("slorii X16 X16 12 252")
    tran0.writeAction("slorii X16 X16 12 1147")
    tran0.writeAction("slorii X16 X16 12 3533")
    tran0.writeAction("srsubii X16 X17 12 147")
    tran0.writeAction("yieldt")
    return efa
