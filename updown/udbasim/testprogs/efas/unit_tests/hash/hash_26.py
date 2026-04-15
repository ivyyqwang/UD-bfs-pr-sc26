from EFA_v2 import *
def hash_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8509231954834480253, 4209295963562065009]
    tran0.writeAction("movir X16 35305")
    tran0.writeAction("slorii X16 X16 12 553")
    tran0.writeAction("slorii X16 X16 12 3828")
    tran0.writeAction("slorii X16 X16 12 2818")
    tran0.writeAction("slorii X16 X16 12 899")
    tran0.writeAction("movir X17 14954")
    tran0.writeAction("slorii X17 X17 12 1734")
    tran0.writeAction("slorii X17 X17 12 134")
    tran0.writeAction("slorii X17 X17 12 2467")
    tran0.writeAction("slorii X17 X17 12 3185")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
