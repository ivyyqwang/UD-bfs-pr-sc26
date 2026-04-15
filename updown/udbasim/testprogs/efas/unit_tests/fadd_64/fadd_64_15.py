from EFA_v2 import *
def fadd_64_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4808264807657838247, 1560425362702198279]
    tran0.writeAction("movir X16 17082")
    tran0.writeAction("slorii X16 X16 12 1589")
    tran0.writeAction("slorii X16 X16 12 3590")
    tran0.writeAction("slorii X16 X16 12 1873")
    tran0.writeAction("slorii X16 X16 12 1703")
    tran0.writeAction("movir X17 5543")
    tran0.writeAction("slorii X17 X17 12 3049")
    tran0.writeAction("slorii X17 X17 12 2450")
    tran0.writeAction("slorii X17 X17 12 1534")
    tran0.writeAction("slorii X17 X17 12 1543")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
