from EFA_v2 import *
def fadd_64_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16566653114271680266, 4805711431369674380]
    tran0.writeAction("movir X16 58856")
    tran0.writeAction("slorii X16 X16 12 2355")
    tran0.writeAction("slorii X16 X16 12 3017")
    tran0.writeAction("slorii X16 X16 12 1156")
    tran0.writeAction("slorii X16 X16 12 1802")
    tran0.writeAction("movir X17 17073")
    tran0.writeAction("slorii X17 X17 12 1297")
    tran0.writeAction("slorii X17 X17 12 1479")
    tran0.writeAction("slorii X17 X17 12 3372")
    tran0.writeAction("slorii X17 X17 12 3724")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
