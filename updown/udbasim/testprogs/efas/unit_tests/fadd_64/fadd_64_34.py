from EFA_v2 import *
def fadd_64_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2774322518049386982, 12252331894879129484]
    tran0.writeAction("movir X16 9856")
    tran0.writeAction("slorii X16 X16 12 1530")
    tran0.writeAction("slorii X16 X16 12 404")
    tran0.writeAction("slorii X16 X16 12 2871")
    tran0.writeAction("slorii X16 X16 12 486")
    tran0.writeAction("movir X17 43529")
    tran0.writeAction("slorii X17 X17 12 111")
    tran0.writeAction("slorii X17 X17 12 344")
    tran0.writeAction("slorii X17 X17 12 1880")
    tran0.writeAction("slorii X17 X17 12 3980")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
