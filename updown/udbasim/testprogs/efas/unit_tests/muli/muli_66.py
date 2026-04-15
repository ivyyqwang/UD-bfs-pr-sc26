from EFA_v2 import *
def muli_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7078276892229524478, -27156]
    tran0.writeAction("movir X16 25147")
    tran0.writeAction("slorii X16 X16 12 373")
    tran0.writeAction("slorii X16 X16 12 1223")
    tran0.writeAction("slorii X16 X16 12 805")
    tran0.writeAction("slorii X16 X16 12 3070")
    tran0.writeAction("muli X16 X17 -27156")
    tran0.writeAction("yieldt")
    return efa
