from EFA_v2 import *
def srorii_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -5877")
    tran0.writeAction("slorii X16 X16 12 2044")
    tran0.writeAction("slorii X16 X16 12 454")
    tran0.writeAction("slorii X16 X16 12 1413")
    tran0.writeAction("slorii X16 X16 12 340")
    tran0.writeAction("movir X17 -9683")
    tran0.writeAction("slorii X17 X17 12 1747")
    tran0.writeAction("slorii X17 X17 12 2150")
    tran0.writeAction("slorii X17 X17 12 538")
    tran0.writeAction("slorii X17 X17 12 1144")
    tran0.writeAction("srorii X16 X17 6 1544")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
