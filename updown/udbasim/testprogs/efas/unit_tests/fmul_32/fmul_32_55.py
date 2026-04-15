from EFA_v2 import *
def fmul_32_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2815669585, 203808212]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 167")
    tran0.writeAction("slorii X16 X16 12 3387")
    tran0.writeAction("slorii X16 X16 12 1361")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 12")
    tran0.writeAction("slorii X17 X17 12 605")
    tran0.writeAction("slorii X17 X17 12 3540")
    tran0.writeAction("fmul.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
