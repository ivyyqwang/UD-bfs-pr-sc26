from EFA_v2 import *
def fmadd_64_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5130899036532796049, 17893557864988496118, 16064555443703702813]
    tran0.writeAction("movir X16 18228")
    tran0.writeAction("slorii X16 X16 12 2519")
    tran0.writeAction("slorii X16 X16 12 3378")
    tran0.writeAction("slorii X16 X16 12 3814")
    tran0.writeAction("slorii X16 X16 12 2705")
    tran0.writeAction("movir X17 63570")
    tran0.writeAction("slorii X17 X17 12 2817")
    tran0.writeAction("slorii X17 X17 12 758")
    tran0.writeAction("slorii X17 X17 12 2197")
    tran0.writeAction("slorii X17 X17 12 246")
    tran0.writeAction("movir X18 57072")
    tran0.writeAction("slorii X18 X18 12 3136")
    tran0.writeAction("slorii X18 X18 12 4088")
    tran0.writeAction("slorii X18 X18 12 2158")
    tran0.writeAction("slorii X18 X18 12 1309")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
