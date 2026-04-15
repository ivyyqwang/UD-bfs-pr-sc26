from EFA_v2 import *
def fadd_64_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17326973577051546910, 13616929551594408398]
    tran0.writeAction("movir X16 61557")
    tran0.writeAction("slorii X16 X16 12 3178")
    tran0.writeAction("slorii X16 X16 12 2692")
    tran0.writeAction("slorii X16 X16 12 3018")
    tran0.writeAction("slorii X16 X16 12 1310")
    tran0.writeAction("movir X17 48377")
    tran0.writeAction("slorii X17 X17 12 212")
    tran0.writeAction("slorii X17 X17 12 2070")
    tran0.writeAction("slorii X17 X17 12 1244")
    tran0.writeAction("slorii X17 X17 12 2510")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
