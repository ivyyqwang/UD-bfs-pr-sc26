from EFA_v2 import *
def fmul_64_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3621066720993272446, 292776248140175367]
    tran0.writeAction("movir X16 12864")
    tran0.writeAction("slorii X16 X16 12 2511")
    tran0.writeAction("slorii X16 X16 12 3932")
    tran0.writeAction("slorii X16 X16 12 3246")
    tran0.writeAction("slorii X16 X16 12 638")
    tran0.writeAction("movir X17 1040")
    tran0.writeAction("slorii X17 X17 12 615")
    tran0.writeAction("slorii X17 X17 12 589")
    tran0.writeAction("slorii X17 X17 12 273")
    tran0.writeAction("slorii X17 X17 12 2055")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
