from EFA_v2 import *
def fadd_64_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [138588666738030111, 12565656100836236041]
    tran0.writeAction("movir X16 492")
    tran0.writeAction("slorii X16 X16 12 1498")
    tran0.writeAction("slorii X16 X16 12 2170")
    tran0.writeAction("slorii X16 X16 12 3339")
    tran0.writeAction("slorii X16 X16 12 1567")
    tran0.writeAction("movir X17 44642")
    tran0.writeAction("slorii X17 X17 12 730")
    tran0.writeAction("slorii X17 X17 12 1508")
    tran0.writeAction("slorii X17 X17 12 261")
    tran0.writeAction("slorii X17 X17 12 2825")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
