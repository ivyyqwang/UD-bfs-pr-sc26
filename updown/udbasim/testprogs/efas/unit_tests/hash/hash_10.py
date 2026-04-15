from EFA_v2 import *
def hash_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [161182735968187635, 1462296072620456677]
    tran0.writeAction("movir X16 572")
    tran0.writeAction("slorii X16 X16 12 2605")
    tran0.writeAction("slorii X16 X16 12 2089")
    tran0.writeAction("slorii X16 X16 12 1267")
    tran0.writeAction("slorii X16 X16 12 1267")
    tran0.writeAction("movir X17 5195")
    tran0.writeAction("slorii X17 X17 12 488")
    tran0.writeAction("slorii X17 X17 12 1996")
    tran0.writeAction("slorii X17 X17 12 4059")
    tran0.writeAction("slorii X17 X17 12 2789")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
