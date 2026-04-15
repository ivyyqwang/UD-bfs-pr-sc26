from EFA_v2 import *
def fadd_64_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12149944225531298983, 10646167686191543205]
    tran0.writeAction("movir X16 43165")
    tran0.writeAction("slorii X16 X16 12 1118")
    tran0.writeAction("slorii X16 X16 12 1635")
    tran0.writeAction("slorii X16 X16 12 2464")
    tran0.writeAction("slorii X16 X16 12 1191")
    tran0.writeAction("movir X17 37822")
    tran0.writeAction("slorii X17 X17 12 3217")
    tran0.writeAction("slorii X17 X17 12 2770")
    tran0.writeAction("slorii X17 X17 12 2823")
    tran0.writeAction("slorii X17 X17 12 933")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
