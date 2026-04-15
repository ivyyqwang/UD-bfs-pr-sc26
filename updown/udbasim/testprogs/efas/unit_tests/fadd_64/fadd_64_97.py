from EFA_v2 import *
def fadd_64_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13503675679203904867, 2917745511712842710]
    tran0.writeAction("movir X16 47974")
    tran0.writeAction("slorii X16 X16 12 2839")
    tran0.writeAction("slorii X16 X16 12 3093")
    tran0.writeAction("slorii X16 X16 12 124")
    tran0.writeAction("slorii X16 X16 12 3427")
    tran0.writeAction("movir X17 10365")
    tran0.writeAction("slorii X17 X17 12 3745")
    tran0.writeAction("slorii X17 X17 12 1410")
    tran0.writeAction("slorii X17 X17 12 2598")
    tran0.writeAction("slorii X17 X17 12 982")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
