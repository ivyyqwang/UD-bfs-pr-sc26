from EFA_v2 import *
def muli_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6501373804676017669, -31603]
    tran0.writeAction("movir X16 42438")
    tran0.writeAction("slorii X16 X16 12 1967")
    tran0.writeAction("slorii X16 X16 12 2156")
    tran0.writeAction("slorii X16 X16 12 1049")
    tran0.writeAction("slorii X16 X16 12 507")
    tran0.writeAction("muli X16 X17 -31603")
    tran0.writeAction("yieldt")
    return efa
