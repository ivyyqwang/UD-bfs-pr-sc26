from EFA_v2 import *
def fdiv_64_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8739221787714434180, 11621398231364862471]
    tran0.writeAction("movir X16 31047")
    tran0.writeAction("slorii X16 X16 12 3902")
    tran0.writeAction("slorii X16 X16 12 2526")
    tran0.writeAction("slorii X16 X16 12 299")
    tran0.writeAction("slorii X16 X16 12 1156")
    tran0.writeAction("movir X17 41287")
    tran0.writeAction("slorii X17 X17 12 2049")
    tran0.writeAction("slorii X17 X17 12 3677")
    tran0.writeAction("slorii X17 X17 12 3504")
    tran0.writeAction("slorii X17 X17 12 519")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
