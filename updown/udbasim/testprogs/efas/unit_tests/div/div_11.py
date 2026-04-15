from EFA_v2 import *
def div_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5632945676386894128, 3904744036866138087]
    tran0.writeAction("movir X16 20012")
    tran0.writeAction("slorii X16 X16 12 995")
    tran0.writeAction("slorii X16 X16 12 3968")
    tran0.writeAction("slorii X16 X16 12 464")
    tran0.writeAction("slorii X16 X16 12 304")
    tran0.writeAction("movir X17 13872")
    tran0.writeAction("slorii X17 X17 12 1792")
    tran0.writeAction("slorii X17 X17 12 872")
    tran0.writeAction("slorii X17 X17 12 945")
    tran0.writeAction("slorii X17 X17 12 4071")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
