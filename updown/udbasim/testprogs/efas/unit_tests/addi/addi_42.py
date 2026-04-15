from EFA_v2 import *
def addi_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1404891348392173726, -6459]
    tran0.writeAction("movir X16 4991")
    tran0.writeAction("slorii X16 X16 12 723")
    tran0.writeAction("slorii X16 X16 12 3304")
    tran0.writeAction("slorii X16 X16 12 3830")
    tran0.writeAction("slorii X16 X16 12 158")
    tran0.writeAction("addi X16 X17 -6459")
    tran0.writeAction("yieldt")
    return efa
