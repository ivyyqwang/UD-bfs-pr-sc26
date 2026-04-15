from EFA_v2 import *
def mul_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7334777477120452768, -3079744261457621572]
    tran0.writeAction("movir X16 26058")
    tran0.writeAction("slorii X16 X16 12 1492")
    tran0.writeAction("slorii X16 X16 12 270")
    tran0.writeAction("slorii X16 X16 12 1230")
    tran0.writeAction("slorii X16 X16 12 2208")
    tran0.writeAction("movir X17 54594")
    tran0.writeAction("slorii X17 X17 12 2254")
    tran0.writeAction("slorii X17 X17 12 2384")
    tran0.writeAction("slorii X17 X17 12 3156")
    tran0.writeAction("slorii X17 X17 12 3516")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
