from EFA_v2 import *
def div_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4017897158430511021, 6632599091859545995]
    tran0.writeAction("movir X16 51261")
    tran0.writeAction("slorii X16 X16 12 2301")
    tran0.writeAction("slorii X16 X16 12 631")
    tran0.writeAction("slorii X16 X16 12 2859")
    tran0.writeAction("slorii X16 X16 12 83")
    tran0.writeAction("movir X17 23563")
    tran0.writeAction("slorii X17 X17 12 2971")
    tran0.writeAction("slorii X17 X17 12 2983")
    tran0.writeAction("slorii X17 X17 12 3549")
    tran0.writeAction("slorii X17 X17 12 3979")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
