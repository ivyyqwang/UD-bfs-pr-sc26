from EFA_v2 import *
def divi_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5768976056535691105, 18748]
    tran0.writeAction("movir X16 20495")
    tran0.writeAction("slorii X16 X16 12 2130")
    tran0.writeAction("slorii X16 X16 12 2167")
    tran0.writeAction("slorii X16 X16 12 2226")
    tran0.writeAction("slorii X16 X16 12 3937")
    tran0.writeAction("divi X16 X17 18748")
    tran0.writeAction("yieldt")
    return efa
