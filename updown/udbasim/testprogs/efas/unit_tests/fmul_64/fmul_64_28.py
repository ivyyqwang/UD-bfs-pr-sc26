from EFA_v2 import *
def fmul_64_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16479533068249637923, 10446545849843017409]
    tran0.writeAction("movir X16 58547")
    tran0.writeAction("slorii X16 X16 12 256")
    tran0.writeAction("slorii X16 X16 12 869")
    tran0.writeAction("slorii X16 X16 12 1322")
    tran0.writeAction("slorii X16 X16 12 1059")
    tran0.writeAction("movir X17 37113")
    tran0.writeAction("slorii X17 X17 12 2401")
    tran0.writeAction("slorii X17 X17 12 2605")
    tran0.writeAction("slorii X17 X17 12 2966")
    tran0.writeAction("slorii X17 X17 12 1729")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
