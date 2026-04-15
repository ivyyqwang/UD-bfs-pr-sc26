from EFA_v2 import *
def fadd_64_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13817762676674578259, 13061718096161363097]
    tran0.writeAction("movir X16 49090")
    tran0.writeAction("slorii X16 X16 12 2271")
    tran0.writeAction("slorii X16 X16 12 477")
    tran0.writeAction("slorii X16 X16 12 3436")
    tran0.writeAction("slorii X16 X16 12 1875")
    tran0.writeAction("movir X17 46404")
    tran0.writeAction("slorii X17 X17 12 2230")
    tran0.writeAction("slorii X17 X17 12 1933")
    tran0.writeAction("slorii X17 X17 12 4053")
    tran0.writeAction("slorii X17 X17 12 1177")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
