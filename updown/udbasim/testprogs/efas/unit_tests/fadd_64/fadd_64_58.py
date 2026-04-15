from EFA_v2 import *
def fadd_64_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5915633373217596409, 9080853503679554581]
    tran0.writeAction("movir X16 21016")
    tran0.writeAction("slorii X16 X16 12 2259")
    tran0.writeAction("slorii X16 X16 12 1512")
    tran0.writeAction("slorii X16 X16 12 330")
    tran0.writeAction("slorii X16 X16 12 1017")
    tran0.writeAction("movir X17 32261")
    tran0.writeAction("slorii X17 X17 12 2754")
    tran0.writeAction("slorii X17 X17 12 1584")
    tran0.writeAction("slorii X17 X17 12 742")
    tran0.writeAction("slorii X17 X17 12 1045")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
