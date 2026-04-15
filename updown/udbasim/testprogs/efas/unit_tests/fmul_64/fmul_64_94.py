from EFA_v2 import *
def fmul_64_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8623148653411182309, 10405691388144280439]
    tran0.writeAction("movir X16 30635")
    tran0.writeAction("slorii X16 X16 12 2368")
    tran0.writeAction("slorii X16 X16 12 843")
    tran0.writeAction("slorii X16 X16 12 3938")
    tran0.writeAction("slorii X16 X16 12 1765")
    tran0.writeAction("movir X17 36968")
    tran0.writeAction("slorii X17 X17 12 1810")
    tran0.writeAction("slorii X17 X17 12 3984")
    tran0.writeAction("slorii X17 X17 12 2790")
    tran0.writeAction("slorii X17 X17 12 887")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
