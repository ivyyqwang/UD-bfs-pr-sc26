from EFA_v2 import *
def evi_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 873
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 10258")
    tran0.writeAction("slorii X16 X16 12 2940")
    tran0.writeAction("slorii X16 X16 12 288")
    tran0.writeAction("slorii X16 X16 12 2956")
    tran0.writeAction("slorii X16 X16 12 3044")
    tran0.writeAction("movir X17 13564")
    tran0.writeAction("slorii X17 X17 12 2937")
    tran0.writeAction("slorii X17 X17 12 3469")
    tran0.writeAction("slorii X17 X17 12 2029")
    tran0.writeAction("slorii X17 X17 12 3081")
    tran0.writeAction("evi X16 X17 873 4")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
