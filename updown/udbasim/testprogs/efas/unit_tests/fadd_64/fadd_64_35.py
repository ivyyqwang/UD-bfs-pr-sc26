from EFA_v2 import *
def fadd_64_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6173478358282603141, 13620935226244708798]
    tran0.writeAction("movir X16 21932")
    tran0.writeAction("slorii X16 X16 12 2461")
    tran0.writeAction("slorii X16 X16 12 3005")
    tran0.writeAction("slorii X16 X16 12 4080")
    tran0.writeAction("slorii X16 X16 12 2693")
    tran0.writeAction("movir X17 48391")
    tran0.writeAction("slorii X17 X17 12 1158")
    tran0.writeAction("slorii X17 X17 12 3044")
    tran0.writeAction("slorii X17 X17 12 3771")
    tran0.writeAction("slorii X17 X17 12 2494")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
