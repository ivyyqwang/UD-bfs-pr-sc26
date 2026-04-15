from EFA_v2 import *
def xori_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -16982")
    tran0.writeAction("slorii X16 X16 12 2296")
    tran0.writeAction("slorii X16 X16 12 629")
    tran0.writeAction("slorii X16 X16 12 2853")
    tran0.writeAction("slorii X16 X16 12 3199")
    tran0.writeAction("movir X17 23196")
    tran0.writeAction("slorii X17 X17 12 1316")
    tran0.writeAction("slorii X17 X17 12 3072")
    tran0.writeAction("slorii X17 X17 12 898")
    tran0.writeAction("slorii X17 X17 12 188")
    tran0.writeAction("xori X16 X17 10579")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
