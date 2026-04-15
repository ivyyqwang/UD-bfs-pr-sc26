from EFA_v2 import *
def evlb_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
        "finish_events": 374500
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 23771")
    tran0.writeAction("slorii X16 X16 12 2329")
    tran0.writeAction("slorii X16 X16 12 2949")
    tran0.writeAction("slorii X16 X16 12 824")
    tran0.writeAction("slorii X16 X16 12 902")
    tran0.writeAction("movir X17 22559")
    tran0.writeAction("slorii X17 X17 12 1738")
    tran0.writeAction("slorii X17 X17 12 2065")
    tran0.writeAction("slorii X17 X17 12 3845")
    tran0.writeAction("slorii X17 X17 12 508")
    tran0.writeAction("evlb X16 374500")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    tran0 = state.writeTransition("eventCarry", state, state, event_map['finish_events'])
    tran0.writeAction("yieldt")
    return efa
