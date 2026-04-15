from EFA_v2 import *
def fadd_64_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8283455984234676229, 1047055079755240509]
    tran0.writeAction("movir X16 29428")
    tran0.writeAction("slorii X16 X16 12 3061")
    tran0.writeAction("slorii X16 X16 12 1148")
    tran0.writeAction("slorii X16 X16 12 3652")
    tran0.writeAction("slorii X16 X16 12 5")
    tran0.writeAction("movir X17 3719")
    tran0.writeAction("slorii X17 X17 12 3632")
    tran0.writeAction("slorii X17 X17 12 3113")
    tran0.writeAction("slorii X17 X17 12 325")
    tran0.writeAction("slorii X17 X17 12 1085")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
