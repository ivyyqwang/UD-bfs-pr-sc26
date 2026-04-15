from EFA_v2 import *
def fdiv_64_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17982308711630623200, 3185844501246206448]
    tran0.writeAction("movir X16 63885")
    tran0.writeAction("slorii X16 X16 12 4071")
    tran0.writeAction("slorii X16 X16 12 4022")
    tran0.writeAction("slorii X16 X16 12 637")
    tran0.writeAction("slorii X16 X16 12 480")
    tran0.writeAction("movir X17 11318")
    tran0.writeAction("slorii X17 X17 12 1611")
    tran0.writeAction("slorii X17 X17 12 462")
    tran0.writeAction("slorii X17 X17 12 1686")
    tran0.writeAction("slorii X17 X17 12 496")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
