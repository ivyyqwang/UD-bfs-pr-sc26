from EFA_v2 import *
def srsubii_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1586882258386374391, 9, 1731]
    tran0.writeAction("movir X16 5637")
    tran0.writeAction("slorii X16 X16 12 3024")
    tran0.writeAction("slorii X16 X16 12 415")
    tran0.writeAction("slorii X16 X16 12 2004")
    tran0.writeAction("slorii X16 X16 12 3831")
    tran0.writeAction("srsubii X16 X17 9 1731")
    tran0.writeAction("yieldt")
    return efa
