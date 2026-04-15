from EFA_v2 import *
def fadd_64_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10884309241172391029, 7205027400269719834]
    tran0.writeAction("movir X16 38668")
    tran0.writeAction("slorii X16 X16 12 3417")
    tran0.writeAction("slorii X16 X16 12 1625")
    tran0.writeAction("slorii X16 X16 12 2383")
    tran0.writeAction("slorii X16 X16 12 1141")
    tran0.writeAction("movir X17 25597")
    tran0.writeAction("slorii X17 X17 12 1635")
    tran0.writeAction("slorii X17 X17 12 3878")
    tran0.writeAction("slorii X17 X17 12 134")
    tran0.writeAction("slorii X17 X17 12 2330")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
