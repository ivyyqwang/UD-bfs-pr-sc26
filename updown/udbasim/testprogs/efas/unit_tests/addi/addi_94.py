from EFA_v2 import *
def addi_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6624601420887242719, -3893]
    tran0.writeAction("movir X16 42000")
    tran0.writeAction("slorii X16 X16 12 2817")
    tran0.writeAction("slorii X16 X16 12 2873")
    tran0.writeAction("slorii X16 X16 12 1916")
    tran0.writeAction("slorii X16 X16 12 2081")
    tran0.writeAction("addi X16 X17 -3893")
    tran0.writeAction("yieldt")
    return efa
