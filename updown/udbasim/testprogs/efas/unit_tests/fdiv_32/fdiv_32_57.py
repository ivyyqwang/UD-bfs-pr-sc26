from EFA_v2 import *
def fdiv_32_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3615587403, 4078230093]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 215")
    tran0.writeAction("slorii X16 X16 12 2071")
    tran0.writeAction("slorii X16 X16 12 3147")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 243")
    tran0.writeAction("slorii X17 X17 12 333")
    tran0.writeAction("slorii X17 X17 12 2637")
    tran0.writeAction("fdiv.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
