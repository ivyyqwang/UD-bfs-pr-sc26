from EFA_v2 import *
def fdiv_64_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5340822401026905423, 8703818840172792079]
    tran0.writeAction("movir X16 18974")
    tran0.writeAction("slorii X16 X16 12 1690")
    tran0.writeAction("slorii X16 X16 12 3397")
    tran0.writeAction("slorii X16 X16 12 2693")
    tran0.writeAction("slorii X16 X16 12 1359")
    tran0.writeAction("movir X17 30922")
    tran0.writeAction("slorii X17 X17 12 721")
    tran0.writeAction("slorii X17 X17 12 3789")
    tran0.writeAction("slorii X17 X17 12 3488")
    tran0.writeAction("slorii X17 X17 12 2319")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
