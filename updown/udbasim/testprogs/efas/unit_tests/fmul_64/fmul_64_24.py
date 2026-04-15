from EFA_v2 import *
def fmul_64_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3926229620556570077, 16786975866610016750]
    tran0.writeAction("movir X16 13948")
    tran0.writeAction("slorii X16 X16 12 3152")
    tran0.writeAction("slorii X16 X16 12 2479")
    tran0.writeAction("slorii X16 X16 12 3649")
    tran0.writeAction("slorii X16 X16 12 3549")
    tran0.writeAction("movir X17 59639")
    tran0.writeAction("slorii X17 X17 12 1305")
    tran0.writeAction("slorii X17 X17 12 3078")
    tran0.writeAction("slorii X17 X17 12 1414")
    tran0.writeAction("slorii X17 X17 12 494")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
