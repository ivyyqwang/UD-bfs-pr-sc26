from EFA_v2 import *
def fdiv_64_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9873616741114652316, 2263428145846425401]
    tran0.writeAction("movir X16 35078")
    tran0.writeAction("slorii X16 X16 12 545")
    tran0.writeAction("slorii X16 X16 12 3334")
    tran0.writeAction("slorii X16 X16 12 2002")
    tran0.writeAction("slorii X16 X16 12 1692")
    tran0.writeAction("movir X17 8041")
    tran0.writeAction("slorii X17 X17 12 1278")
    tran0.writeAction("slorii X17 X17 12 2063")
    tran0.writeAction("slorii X17 X17 12 3265")
    tran0.writeAction("slorii X17 X17 12 1849")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
