from EFA_v2 import *
def mod_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8295694559338267971, 3694804860886279462]
    tran0.writeAction("movir X16 36063")
    tran0.writeAction("slorii X16 X16 12 3164")
    tran0.writeAction("slorii X16 X16 12 49")
    tran0.writeAction("slorii X16 X16 12 2055")
    tran0.writeAction("slorii X16 X16 12 2749")
    tran0.writeAction("movir X17 13126")
    tran0.writeAction("slorii X17 X17 12 2391")
    tran0.writeAction("slorii X17 X17 12 495")
    tran0.writeAction("slorii X17 X17 12 2102")
    tran0.writeAction("slorii X17 X17 12 1318")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
