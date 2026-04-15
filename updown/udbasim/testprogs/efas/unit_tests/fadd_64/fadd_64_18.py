from EFA_v2 import *
def fadd_64_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14449359972532775777, 7813078357650883582]
    tran0.writeAction("movir X16 51334")
    tran0.writeAction("slorii X16 X16 12 1797")
    tran0.writeAction("slorii X16 X16 12 1738")
    tran0.writeAction("slorii X16 X16 12 2310")
    tran0.writeAction("slorii X16 X16 12 2913")
    tran0.writeAction("movir X17 27757")
    tran0.writeAction("slorii X17 X17 12 2581")
    tran0.writeAction("slorii X17 X17 12 3822")
    tran0.writeAction("slorii X17 X17 12 300")
    tran0.writeAction("slorii X17 X17 12 1022")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
