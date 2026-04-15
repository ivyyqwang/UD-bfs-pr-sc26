from EFA_v2 import *
def muli_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6276198241181844873, 29837]
    tran0.writeAction("movir X16 22297")
    tran0.writeAction("slorii X16 X16 12 2192")
    tran0.writeAction("slorii X16 X16 12 3121")
    tran0.writeAction("slorii X16 X16 12 2356")
    tran0.writeAction("slorii X16 X16 12 1417")
    tran0.writeAction("muli X16 X17 29837")
    tran0.writeAction("yieldt")
    return efa
