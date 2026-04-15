from EFA_v2 import *
def muli_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9105008890160897039, -30430]
    tran0.writeAction("movir X16 32347")
    tran0.writeAction("slorii X16 X16 12 2005")
    tran0.writeAction("slorii X16 X16 12 2142")
    tran0.writeAction("slorii X16 X16 12 3333")
    tran0.writeAction("slorii X16 X16 12 3087")
    tran0.writeAction("muli X16 X17 -30430")
    tran0.writeAction("yieldt")
    return efa
