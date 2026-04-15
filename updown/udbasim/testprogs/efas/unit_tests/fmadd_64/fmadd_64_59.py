from EFA_v2 import *
def fmadd_64_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2023867482938971974, 7724902534422658662, 9808013830237057599]
    tran0.writeAction("movir X16 7190")
    tran0.writeAction("slorii X16 X16 12 908")
    tran0.writeAction("slorii X16 X16 12 185")
    tran0.writeAction("slorii X16 X16 12 169")
    tran0.writeAction("slorii X16 X16 12 1862")
    tran0.writeAction("movir X17 27444")
    tran0.writeAction("slorii X17 X17 12 1502")
    tran0.writeAction("slorii X17 X17 12 3392")
    tran0.writeAction("slorii X17 X17 12 3183")
    tran0.writeAction("slorii X17 X17 12 3686")
    tran0.writeAction("movir X18 34845")
    tran0.writeAction("slorii X18 X18 12 265")
    tran0.writeAction("slorii X18 X18 12 3343")
    tran0.writeAction("slorii X18 X18 12 1631")
    tran0.writeAction("slorii X18 X18 12 575")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
