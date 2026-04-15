from EFA_v2 import *
def div_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7846832655270571611, 7559387976057134162]
    tran0.writeAction("movir X16 27877")
    tran0.writeAction("slorii X16 X16 12 2251")
    tran0.writeAction("slorii X16 X16 12 2501")
    tran0.writeAction("slorii X16 X16 12 1382")
    tran0.writeAction("slorii X16 X16 12 3675")
    tran0.writeAction("movir X17 26856")
    tran0.writeAction("slorii X17 X17 12 1397")
    tran0.writeAction("slorii X17 X17 12 24")
    tran0.writeAction("slorii X17 X17 12 1001")
    tran0.writeAction("slorii X17 X17 12 3154")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
