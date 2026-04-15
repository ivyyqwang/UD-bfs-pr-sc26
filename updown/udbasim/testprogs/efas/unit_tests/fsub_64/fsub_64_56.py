from EFA_v2 import *
def fsub_64_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15323160580536763384, 18255574450030832356]
    tran0.writeAction("movir X16 54438")
    tran0.writeAction("slorii X16 X16 12 3285")
    tran0.writeAction("slorii X16 X16 12 3271")
    tran0.writeAction("slorii X16 X16 12 664")
    tran0.writeAction("slorii X16 X16 12 1016")
    tran0.writeAction("movir X17 64856")
    tran0.writeAction("slorii X17 X17 12 3395")
    tran0.writeAction("slorii X17 X17 12 3448")
    tran0.writeAction("slorii X17 X17 12 3214")
    tran0.writeAction("slorii X17 X17 12 2788")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
