from EFA_v2 import *
def sub_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3157032496133275032, -512304548234373567]
    tran0.writeAction("movir X16 54319")
    tran0.writeAction("slorii X16 X16 12 3962")
    tran0.writeAction("slorii X16 X16 12 3043")
    tran0.writeAction("slorii X16 X16 12 2504")
    tran0.writeAction("slorii X16 X16 12 616")
    tran0.writeAction("movir X17 63715")
    tran0.writeAction("slorii X17 X17 12 3803")
    tran0.writeAction("slorii X17 X17 12 2633")
    tran0.writeAction("slorii X17 X17 12 2757")
    tran0.writeAction("slorii X17 X17 12 1601")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
