from EFA_v2 import *
def div_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5120774956562269883, 56606374668886007]
    tran0.writeAction("movir X16 47343")
    tran0.writeAction("slorii X16 X16 12 1444")
    tran0.writeAction("slorii X16 X16 12 3803")
    tran0.writeAction("slorii X16 X16 12 1595")
    tran0.writeAction("slorii X16 X16 12 2373")
    tran0.writeAction("movir X17 201")
    tran0.writeAction("slorii X17 X17 12 435")
    tran0.writeAction("slorii X17 X17 12 678")
    tran0.writeAction("slorii X17 X17 12 661")
    tran0.writeAction("slorii X17 X17 12 4087")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
