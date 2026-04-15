from EFA_v2 import *
def fdiv_32_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1338623350, 1005272041]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 79")
    tran0.writeAction("slorii X16 X16 12 3228")
    tran0.writeAction("slorii X16 X16 12 1398")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 59")
    tran0.writeAction("slorii X17 X17 12 3763")
    tran0.writeAction("slorii X17 X17 12 3049")
    tran0.writeAction("fdiv.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
