from EFA_v2 import *
def fmul_64_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11715102485482045078, 17180716542123963226]
    tran0.writeAction("movir X16 41620")
    tran0.writeAction("slorii X16 X16 12 1658")
    tran0.writeAction("slorii X16 X16 12 1066")
    tran0.writeAction("slorii X16 X16 12 1855")
    tran0.writeAction("slorii X16 X16 12 3734")
    tran0.writeAction("movir X17 61038")
    tran0.writeAction("slorii X17 X17 12 682")
    tran0.writeAction("slorii X17 X17 12 2799")
    tran0.writeAction("slorii X17 X17 12 3999")
    tran0.writeAction("slorii X17 X17 12 858")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
