from EFA_v2 import *
def fadd_64_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17290395583330310786, 11779941063464977534]
    tran0.writeAction("movir X16 61427")
    tran0.writeAction("slorii X16 X16 12 3378")
    tran0.writeAction("slorii X16 X16 12 3250")
    tran0.writeAction("slorii X16 X16 12 1581")
    tran0.writeAction("slorii X16 X16 12 2690")
    tran0.writeAction("movir X17 41850")
    tran0.writeAction("slorii X17 X17 12 3103")
    tran0.writeAction("slorii X17 X17 12 3074")
    tran0.writeAction("slorii X17 X17 12 3552")
    tran0.writeAction("slorii X17 X17 12 1150")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
