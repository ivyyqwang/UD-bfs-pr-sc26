from EFA_v2 import *
def div_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3361660782398184352, 6876286076517849613]
    tran0.writeAction("movir X16 53592")
    tran0.writeAction("slorii X16 X16 12 4021")
    tran0.writeAction("slorii X16 X16 12 1097")
    tran0.writeAction("slorii X16 X16 12 3254")
    tran0.writeAction("slorii X16 X16 12 1120")
    tran0.writeAction("movir X17 24429")
    tran0.writeAction("slorii X17 X17 12 1948")
    tran0.writeAction("slorii X17 X17 12 292")
    tran0.writeAction("slorii X17 X17 12 3321")
    tran0.writeAction("slorii X17 X17 12 2573")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
