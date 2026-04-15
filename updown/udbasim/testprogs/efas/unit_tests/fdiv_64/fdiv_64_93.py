from EFA_v2 import *
def fdiv_64_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1652046335114462938, 4026452811452063129]
    tran0.writeAction("movir X16 5869")
    tran0.writeAction("slorii X16 X16 12 1014")
    tran0.writeAction("slorii X16 X16 12 908")
    tran0.writeAction("slorii X16 X16 12 4028")
    tran0.writeAction("slorii X16 X16 12 1754")
    tran0.writeAction("movir X17 14304")
    tran0.writeAction("slorii X17 X17 12 3415")
    tran0.writeAction("slorii X17 X17 12 4027")
    tran0.writeAction("slorii X17 X17 12 1937")
    tran0.writeAction("slorii X17 X17 12 3481")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
