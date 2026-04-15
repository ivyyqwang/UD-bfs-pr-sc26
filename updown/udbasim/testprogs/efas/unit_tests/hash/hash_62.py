from EFA_v2 import *
def hash_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8277281633282652620, 2586848011353775782]
    tran0.writeAction("movir X16 36129")
    tran0.writeAction("slorii X16 X16 12 771")
    tran0.writeAction("slorii X16 X16 12 1438")
    tran0.writeAction("slorii X16 X16 12 1320")
    tran0.writeAction("slorii X16 X16 12 1588")
    tran0.writeAction("movir X17 9190")
    tran0.writeAction("slorii X17 X17 12 1352")
    tran0.writeAction("slorii X17 X17 12 3972")
    tran0.writeAction("slorii X17 X17 12 2733")
    tran0.writeAction("slorii X17 X17 12 3750")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
