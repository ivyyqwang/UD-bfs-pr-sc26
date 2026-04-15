from EFA_v2 import *
def fmul_64_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11187419121635649919, 12909766866763052624]
    tran0.writeAction("movir X16 39745")
    tran0.writeAction("slorii X16 X16 12 2854")
    tran0.writeAction("slorii X16 X16 12 2794")
    tran0.writeAction("slorii X16 X16 12 2070")
    tran0.writeAction("slorii X16 X16 12 2431")
    tran0.writeAction("movir X17 45864")
    tran0.writeAction("slorii X17 X17 12 2889")
    tran0.writeAction("slorii X17 X17 12 258")
    tran0.writeAction("slorii X17 X17 12 2127")
    tran0.writeAction("slorii X17 X17 12 1616")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
