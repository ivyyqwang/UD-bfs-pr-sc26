from EFA_v2 import *
def muli_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5147182760385039059, -27926]
    tran0.writeAction("movir X16 18286")
    tran0.writeAction("slorii X16 X16 12 1911")
    tran0.writeAction("slorii X16 X16 12 794")
    tran0.writeAction("slorii X16 X16 12 3132")
    tran0.writeAction("slorii X16 X16 12 2771")
    tran0.writeAction("muli X16 X17 -27926")
    tran0.writeAction("yieldt")
    return efa
