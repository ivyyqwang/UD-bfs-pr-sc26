from EFA_v2 import *
def fadd_64_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14264560522908336255, 8688650569941954872]
    tran0.writeAction("movir X16 50677")
    tran0.writeAction("slorii X16 X16 12 3683")
    tran0.writeAction("slorii X16 X16 12 2045")
    tran0.writeAction("slorii X16 X16 12 48")
    tran0.writeAction("slorii X16 X16 12 127")
    tran0.writeAction("movir X17 30868")
    tran0.writeAction("slorii X17 X17 12 1178")
    tran0.writeAction("slorii X17 X17 12 2222")
    tran0.writeAction("slorii X17 X17 12 3627")
    tran0.writeAction("slorii X17 X17 12 312")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
