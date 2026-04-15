from EFA_v2 import *
def fadd_32_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1978596165, 766949751]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 117")
    tran0.writeAction("slorii X16 X16 12 3823")
    tran0.writeAction("slorii X16 X16 12 2885")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 45")
    tran0.writeAction("slorii X17 X17 12 2923")
    tran0.writeAction("slorii X17 X17 12 2423")
    tran0.writeAction("fadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
