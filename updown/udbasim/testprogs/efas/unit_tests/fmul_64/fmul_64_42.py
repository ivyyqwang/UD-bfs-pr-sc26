from EFA_v2 import *
def fmul_64_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9600578272632588152, 11365094377791255930]
    tran0.writeAction("movir X16 34108")
    tran0.writeAction("slorii X16 X16 12 433")
    tran0.writeAction("slorii X16 X16 12 682")
    tran0.writeAction("slorii X16 X16 12 2452")
    tran0.writeAction("slorii X16 X16 12 1912")
    tran0.writeAction("movir X17 40376")
    tran0.writeAction("slorii X17 X17 12 3793")
    tran0.writeAction("slorii X17 X17 12 3883")
    tran0.writeAction("slorii X17 X17 12 151")
    tran0.writeAction("slorii X17 X17 12 1402")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
