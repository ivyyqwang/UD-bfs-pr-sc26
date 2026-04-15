from EFA_v2 import *
def hash_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4465968481184311214, 4600725916250952429]
    tran0.writeAction("movir X16 49669")
    tran0.writeAction("slorii X16 X16 12 2837")
    tran0.writeAction("slorii X16 X16 12 1020")
    tran0.writeAction("slorii X16 X16 12 3761")
    tran0.writeAction("slorii X16 X16 12 2130")
    tran0.writeAction("movir X17 16345")
    tran0.writeAction("slorii X17 X17 12 253")
    tran0.writeAction("slorii X17 X17 12 2139")
    tran0.writeAction("slorii X17 X17 12 293")
    tran0.writeAction("slorii X17 X17 12 749")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
