from EFA_v2 import *
def fadd_64_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1508755744066920954, 7275204330687727748]
    tran0.writeAction("movir X16 5360")
    tran0.writeAction("slorii X16 X16 12 725")
    tran0.writeAction("slorii X16 X16 12 2817")
    tran0.writeAction("slorii X16 X16 12 3846")
    tran0.writeAction("slorii X16 X16 12 506")
    tran0.writeAction("movir X17 25846")
    tran0.writeAction("slorii X17 X17 12 2940")
    tran0.writeAction("slorii X17 X17 12 2823")
    tran0.writeAction("slorii X17 X17 12 104")
    tran0.writeAction("slorii X17 X17 12 2180")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
