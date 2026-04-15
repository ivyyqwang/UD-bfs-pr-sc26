from EFA_v2 import *
def fadd_64_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18274172534065583035, 3954418435722545424]
    tran0.writeAction("movir X16 64922")
    tran0.writeAction("slorii X16 X16 12 3697")
    tran0.writeAction("slorii X16 X16 12 2393")
    tran0.writeAction("slorii X16 X16 12 733")
    tran0.writeAction("slorii X16 X16 12 955")
    tran0.writeAction("movir X17 14048")
    tran0.writeAction("slorii X17 X17 12 3753")
    tran0.writeAction("slorii X17 X17 12 3498")
    tran0.writeAction("slorii X17 X17 12 2040")
    tran0.writeAction("slorii X17 X17 12 2320")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
