from EFA_v2 import *
def fadd_64_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1552287572666461640, 2762589744985392293]
    tran0.writeAction("movir X16 5514")
    tran0.writeAction("slorii X16 X16 12 3413")
    tran0.writeAction("slorii X16 X16 12 686")
    tran0.writeAction("slorii X16 X16 12 154")
    tran0.writeAction("slorii X16 X16 12 3528")
    tran0.writeAction("movir X17 9814")
    tran0.writeAction("slorii X17 X17 12 2827")
    tran0.writeAction("slorii X17 X17 12 3193")
    tran0.writeAction("slorii X17 X17 12 4060")
    tran0.writeAction("slorii X17 X17 12 1189")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
