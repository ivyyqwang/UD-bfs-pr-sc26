from EFA_v2 import *
def muli_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4542204906476899145, -3697]
    tran0.writeAction("movir X16 16137")
    tran0.writeAction("slorii X16 X16 12 628")
    tran0.writeAction("slorii X16 X16 12 3067")
    tran0.writeAction("slorii X16 X16 12 2424")
    tran0.writeAction("slorii X16 X16 12 2889")
    tran0.writeAction("muli X16 X17 -3697")
    tran0.writeAction("yieldt")
    return efa
