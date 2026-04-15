from EFA_v2 import *
def srsubii_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1265903885899120275, 0, 856]
    tran0.writeAction("movir X16 4497")
    tran0.writeAction("slorii X16 X16 12 1614")
    tran0.writeAction("slorii X16 X16 12 142")
    tran0.writeAction("slorii X16 X16 12 3291")
    tran0.writeAction("slorii X16 X16 12 3731")
    tran0.writeAction("srsubii X16 X17 0 856")
    tran0.writeAction("yieldt")
    return efa
