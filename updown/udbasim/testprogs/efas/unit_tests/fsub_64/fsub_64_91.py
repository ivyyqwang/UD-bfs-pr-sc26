from EFA_v2 import *
def fsub_64_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [827075980571003670, 8924714958133193783]
    tran0.writeAction("movir X16 2938")
    tran0.writeAction("slorii X16 X16 12 1491")
    tran0.writeAction("slorii X16 X16 12 2280")
    tran0.writeAction("slorii X16 X16 12 788")
    tran0.writeAction("slorii X16 X16 12 2838")
    tran0.writeAction("movir X17 31706")
    tran0.writeAction("slorii X17 X17 12 3919")
    tran0.writeAction("slorii X17 X17 12 2081")
    tran0.writeAction("slorii X17 X17 12 590")
    tran0.writeAction("slorii X17 X17 12 3127")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
