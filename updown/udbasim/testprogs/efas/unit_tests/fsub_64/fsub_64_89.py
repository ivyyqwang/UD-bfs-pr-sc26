from EFA_v2 import *
def fsub_64_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9663340885532289320, 15222611959649914308]
    tran0.writeAction("movir X16 34331")
    tran0.writeAction("slorii X16 X16 12 341")
    tran0.writeAction("slorii X16 X16 12 1593")
    tran0.writeAction("slorii X16 X16 12 2706")
    tran0.writeAction("slorii X16 X16 12 2344")
    tran0.writeAction("movir X17 54081")
    tran0.writeAction("slorii X17 X17 12 2382")
    tran0.writeAction("slorii X17 X17 12 3240")
    tran0.writeAction("slorii X17 X17 12 2236")
    tran0.writeAction("slorii X17 X17 12 3524")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
