from EFA_v2 import *
def fmul_64_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10775741561385219702, 4968050251479265509]
    tran0.writeAction("movir X16 38283")
    tran0.writeAction("slorii X16 X16 12 509")
    tran0.writeAction("slorii X16 X16 12 2965")
    tran0.writeAction("slorii X16 X16 12 3191")
    tran0.writeAction("slorii X16 X16 12 1654")
    tran0.writeAction("movir X17 17650")
    tran0.writeAction("slorii X17 X17 12 246")
    tran0.writeAction("slorii X17 X17 12 449")
    tran0.writeAction("slorii X17 X17 12 2915")
    tran0.writeAction("slorii X17 X17 12 229")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
