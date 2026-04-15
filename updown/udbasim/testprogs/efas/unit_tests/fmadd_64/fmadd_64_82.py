from EFA_v2 import *
def fmadd_64_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17543181473547229146, 12890791405036746015, 3940416983421894599]
    tran0.writeAction("movir X16 62325")
    tran0.writeAction("slorii X16 X16 12 3689")
    tran0.writeAction("slorii X16 X16 12 2616")
    tran0.writeAction("slorii X16 X16 12 4081")
    tran0.writeAction("slorii X16 X16 12 2010")
    tran0.writeAction("movir X17 45797")
    tran0.writeAction("slorii X17 X17 12 1191")
    tran0.writeAction("slorii X17 X17 12 3082")
    tran0.writeAction("slorii X17 X17 12 3579")
    tran0.writeAction("slorii X17 X17 12 1311")
    tran0.writeAction("movir X18 13999")
    tran0.writeAction("slorii X18 X18 12 709")
    tran0.writeAction("slorii X18 X18 12 3715")
    tran0.writeAction("slorii X18 X18 12 3187")
    tran0.writeAction("slorii X18 X18 12 4039")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
