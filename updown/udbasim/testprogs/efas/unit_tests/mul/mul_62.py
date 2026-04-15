from EFA_v2 import *
def mul_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1988033081942126234, -6504730255078758559]
    tran0.writeAction("movir X16 7062")
    tran0.writeAction("slorii X16 X16 12 3736")
    tran0.writeAction("slorii X16 X16 12 3602")
    tran0.writeAction("slorii X16 X16 12 3626")
    tran0.writeAction("slorii X16 X16 12 3738")
    tran0.writeAction("movir X17 42426")
    tran0.writeAction("slorii X17 X17 12 2276")
    tran0.writeAction("slorii X17 X17 12 3050")
    tran0.writeAction("slorii X17 X17 12 1206")
    tran0.writeAction("slorii X17 X17 12 1889")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
