from EFA_v2 import *
def fadd_64_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18129273251254248253, 2947945390152465462]
    tran0.writeAction("movir X16 64408")
    tran0.writeAction("slorii X16 X16 12 479")
    tran0.writeAction("slorii X16 X16 12 2065")
    tran0.writeAction("slorii X16 X16 12 2")
    tran0.writeAction("slorii X16 X16 12 829")
    tran0.writeAction("movir X17 10473")
    tran0.writeAction("slorii X17 X17 12 843")
    tran0.writeAction("slorii X17 X17 12 1701")
    tran0.writeAction("slorii X17 X17 12 1179")
    tran0.writeAction("slorii X17 X17 12 3126")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
