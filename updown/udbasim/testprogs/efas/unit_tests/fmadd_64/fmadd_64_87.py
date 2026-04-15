from EFA_v2 import *
def fmadd_64_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3491821724680833737, 11396966233895495915, 92972676389684700]
    tran0.writeAction("movir X16 12405")
    tran0.writeAction("slorii X16 X16 12 1813")
    tran0.writeAction("slorii X16 X16 12 2990")
    tran0.writeAction("slorii X16 X16 12 2428")
    tran0.writeAction("slorii X16 X16 12 2761")
    tran0.writeAction("movir X17 40490")
    tran0.writeAction("slorii X17 X17 12 646")
    tran0.writeAction("slorii X17 X17 12 2032")
    tran0.writeAction("slorii X17 X17 12 1894")
    tran0.writeAction("slorii X17 X17 12 2283")
    tran0.writeAction("movir X18 330")
    tran0.writeAction("slorii X18 X18 12 1250")
    tran0.writeAction("slorii X18 X18 12 2070")
    tran0.writeAction("slorii X18 X18 12 100")
    tran0.writeAction("slorii X18 X18 12 1500")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
