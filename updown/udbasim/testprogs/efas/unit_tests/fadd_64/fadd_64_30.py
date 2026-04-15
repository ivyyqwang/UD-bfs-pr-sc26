from EFA_v2 import *
def fadd_64_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7849733231427851334, 3144012341488782085]
    tran0.writeAction("movir X16 27887")
    tran0.writeAction("slorii X16 X16 12 3500")
    tran0.writeAction("slorii X16 X16 12 2248")
    tran0.writeAction("slorii X16 X16 12 3425")
    tran0.writeAction("slorii X16 X16 12 1094")
    tran0.writeAction("movir X17 11169")
    tran0.writeAction("slorii X17 X17 12 3177")
    tran0.writeAction("slorii X17 X17 12 287")
    tran0.writeAction("slorii X17 X17 12 3616")
    tran0.writeAction("slorii X17 X17 12 2821")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
