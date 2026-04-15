from EFA_v2 import *
def mod_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4509500177001816794, 2156183210237057318]
    tran0.writeAction("movir X16 16020")
    tran0.writeAction("slorii X16 X16 12 3944")
    tran0.writeAction("slorii X16 X16 12 1220")
    tran0.writeAction("slorii X16 X16 12 3090")
    tran0.writeAction("slorii X16 X16 12 730")
    tran0.writeAction("movir X17 7660")
    tran0.writeAction("slorii X17 X17 12 1235")
    tran0.writeAction("slorii X17 X17 12 1196")
    tran0.writeAction("slorii X17 X17 12 3445")
    tran0.writeAction("slorii X17 X17 12 2342")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
