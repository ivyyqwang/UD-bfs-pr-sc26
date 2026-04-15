from EFA_v2 import *
def fdiv_64_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2530387794919032425, 13344950216874396854]
    tran0.writeAction("movir X16 8989")
    tran0.writeAction("slorii X16 X16 12 3044")
    tran0.writeAction("slorii X16 X16 12 2812")
    tran0.writeAction("slorii X16 X16 12 544")
    tran0.writeAction("slorii X16 X16 12 1641")
    tran0.writeAction("movir X17 47410")
    tran0.writeAction("slorii X17 X17 12 3224")
    tran0.writeAction("slorii X17 X17 12 1158")
    tran0.writeAction("slorii X17 X17 12 288")
    tran0.writeAction("slorii X17 X17 12 3254")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
