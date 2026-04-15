from EFA_v2 import *
def fdiv_64_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8699142213498588281, 11532532137233633903]
    tran0.writeAction("movir X16 30905")
    tran0.writeAction("slorii X16 X16 12 2300")
    tran0.writeAction("slorii X16 X16 12 206")
    tran0.writeAction("slorii X16 X16 12 772")
    tran0.writeAction("slorii X16 X16 12 3193")
    tran0.writeAction("movir X17 40971")
    tran0.writeAction("slorii X17 X17 12 3214")
    tran0.writeAction("slorii X17 X17 12 120")
    tran0.writeAction("slorii X17 X17 12 2405")
    tran0.writeAction("slorii X17 X17 12 623")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
