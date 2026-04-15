from EFA_v2 import *
def fmul_64_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14223716933965507363, 9193297781272456091]
    tran0.writeAction("movir X16 50532")
    tran0.writeAction("slorii X16 X16 12 3251")
    tran0.writeAction("slorii X16 X16 12 226")
    tran0.writeAction("slorii X16 X16 12 2958")
    tran0.writeAction("slorii X16 X16 12 2851")
    tran0.writeAction("movir X17 32661")
    tran0.writeAction("slorii X17 X17 12 633")
    tran0.writeAction("slorii X17 X17 12 4023")
    tran0.writeAction("slorii X17 X17 12 538")
    tran0.writeAction("slorii X17 X17 12 2971")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
