from EFA_v2 import *
def fadd_64_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8018436635740589560, 17590787336469068229]
    tran0.writeAction("movir X16 28487")
    tran0.writeAction("slorii X16 X16 12 858")
    tran0.writeAction("slorii X16 X16 12 767")
    tran0.writeAction("slorii X16 X16 12 1212")
    tran0.writeAction("slorii X16 X16 12 3576")
    tran0.writeAction("movir X17 62495")
    tran0.writeAction("slorii X17 X17 12 126")
    tran0.writeAction("slorii X17 X17 12 493")
    tran0.writeAction("slorii X17 X17 12 2779")
    tran0.writeAction("slorii X17 X17 12 2501")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
