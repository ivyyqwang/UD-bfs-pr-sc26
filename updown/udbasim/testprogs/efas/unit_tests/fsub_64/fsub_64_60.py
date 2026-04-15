from EFA_v2 import *
def fsub_64_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17919482143458592863, 148121244977498306]
    tran0.writeAction("movir X16 63662")
    tran0.writeAction("slorii X16 X16 12 3233")
    tran0.writeAction("slorii X16 X16 12 359")
    tran0.writeAction("slorii X16 X16 12 3296")
    tran0.writeAction("slorii X16 X16 12 2143")
    tran0.writeAction("movir X17 526")
    tran0.writeAction("slorii X17 X17 12 951")
    tran0.writeAction("slorii X17 X17 12 3278")
    tran0.writeAction("slorii X17 X17 12 2344")
    tran0.writeAction("slorii X17 X17 12 2242")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
