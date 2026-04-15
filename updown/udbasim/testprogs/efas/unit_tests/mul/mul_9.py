from EFA_v2 import *
def mul_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1473269662359748912, -394910522375499746]
    tran0.writeAction("movir X16 60301")
    tran0.writeAction("slorii X16 X16 12 3664")
    tran0.writeAction("slorii X16 X16 12 3132")
    tran0.writeAction("slorii X16 X16 12 2815")
    tran0.writeAction("slorii X16 X16 12 3792")
    tran0.writeAction("movir X17 64132")
    tran0.writeAction("slorii X17 X17 12 4079")
    tran0.writeAction("slorii X17 X17 12 2275")
    tran0.writeAction("slorii X17 X17 12 3049")
    tran0.writeAction("slorii X17 X17 12 30")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
