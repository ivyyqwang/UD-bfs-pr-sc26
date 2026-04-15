from EFA_v2 import *
def div_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2342203130885113570, -841709104480850680]
    tran0.writeAction("movir X16 8321")
    tran0.writeAction("slorii X16 X16 12 725")
    tran0.writeAction("slorii X16 X16 12 1672")
    tran0.writeAction("slorii X16 X16 12 880")
    tran0.writeAction("slorii X16 X16 12 1762")
    tran0.writeAction("movir X17 62545")
    tran0.writeAction("slorii X17 X17 12 2656")
    tran0.writeAction("slorii X17 X17 12 1903")
    tran0.writeAction("slorii X17 X17 12 846")
    tran0.writeAction("slorii X17 X17 12 3336")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
