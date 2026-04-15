from EFA_v2 import *
def divi_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8783806676216588225, 1353]
    tran0.writeAction("movir X16 31206")
    tran0.writeAction("slorii X16 X16 12 1434")
    tran0.writeAction("slorii X16 X16 12 551")
    tran0.writeAction("slorii X16 X16 12 2434")
    tran0.writeAction("slorii X16 X16 12 1985")
    tran0.writeAction("divi X16 X17 1353")
    tran0.writeAction("yieldt")
    return efa
