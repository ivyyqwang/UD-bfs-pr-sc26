from EFA_v2 import *
def fmul_64_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18293536907452919899, 7149787116891424088]
    tran0.writeAction("movir X16 64991")
    tran0.writeAction("slorii X16 X16 12 2862")
    tran0.writeAction("slorii X16 X16 12 1246")
    tran0.writeAction("slorii X16 X16 12 939")
    tran0.writeAction("slorii X16 X16 12 91")
    tran0.writeAction("movir X17 25401")
    tran0.writeAction("slorii X17 X17 12 600")
    tran0.writeAction("slorii X17 X17 12 105")
    tran0.writeAction("slorii X17 X17 12 4004")
    tran0.writeAction("slorii X17 X17 12 1368")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
