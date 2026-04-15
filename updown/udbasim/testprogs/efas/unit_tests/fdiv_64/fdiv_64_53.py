from EFA_v2 import *
def fdiv_64_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1737009454056808113, 2273119612420384101]
    tran0.writeAction("movir X16 6171")
    tran0.writeAction("slorii X16 X16 12 398")
    tran0.writeAction("slorii X16 X16 12 1336")
    tran0.writeAction("slorii X16 X16 12 2257")
    tran0.writeAction("slorii X16 X16 12 3761")
    tran0.writeAction("movir X17 8075")
    tran0.writeAction("slorii X17 X17 12 3043")
    tran0.writeAction("slorii X17 X17 12 3702")
    tran0.writeAction("slorii X17 X17 12 1190")
    tran0.writeAction("slorii X17 X17 12 1381")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
