from EFA_v2 import *
def fsub_64_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15230083352118564727, 8890749928895301062]
    tran0.writeAction("movir X16 54108")
    tran0.writeAction("slorii X16 X16 12 513")
    tran0.writeAction("slorii X16 X16 12 3526")
    tran0.writeAction("slorii X16 X16 12 2529")
    tran0.writeAction("slorii X16 X16 12 1911")
    tran0.writeAction("movir X17 31586")
    tran0.writeAction("slorii X17 X17 12 1183")
    tran0.writeAction("slorii X17 X17 12 1154")
    tran0.writeAction("slorii X17 X17 12 2596")
    tran0.writeAction("slorii X17 X17 12 1478")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
