from EFA_v2 import *
def fmul_64_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12944896877740686000, 2187986649929427119]
    tran0.writeAction("movir X16 45989")
    tran0.writeAction("slorii X16 X16 12 2098")
    tran0.writeAction("slorii X16 X16 12 19")
    tran0.writeAction("slorii X16 X16 12 3263")
    tran0.writeAction("slorii X16 X16 12 2736")
    tran0.writeAction("movir X17 7773")
    tran0.writeAction("slorii X17 X17 12 1188")
    tran0.writeAction("slorii X17 X17 12 1026")
    tran0.writeAction("slorii X17 X17 12 1394")
    tran0.writeAction("slorii X17 X17 12 2223")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
