from EFA_v2 import *
def fdiv_64_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11293433023826543712, 10810276304541910106]
    tran0.writeAction("movir X16 40122")
    tran0.writeAction("slorii X16 X16 12 1367")
    tran0.writeAction("slorii X16 X16 12 4095")
    tran0.writeAction("slorii X16 X16 12 3468")
    tran0.writeAction("slorii X16 X16 12 1120")
    tran0.writeAction("movir X17 38405")
    tran0.writeAction("slorii X17 X17 12 3344")
    tran0.writeAction("slorii X17 X17 12 1552")
    tran0.writeAction("slorii X17 X17 12 176")
    tran0.writeAction("slorii X17 X17 12 1114")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
