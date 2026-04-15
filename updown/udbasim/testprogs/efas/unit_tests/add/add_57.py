from EFA_v2 import *
def add_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6900635779344259570, -5668503239240541316]
    tran0.writeAction("movir X16 41020")
    tran0.writeAction("slorii X16 X16 12 69")
    tran0.writeAction("slorii X16 X16 12 479")
    tran0.writeAction("slorii X16 X16 12 3418")
    tran0.writeAction("slorii X16 X16 12 1550")
    tran0.writeAction("movir X17 45397")
    tran0.writeAction("slorii X17 X17 12 1765")
    tran0.writeAction("slorii X17 X17 12 1600")
    tran0.writeAction("slorii X17 X17 12 3753")
    tran0.writeAction("slorii X17 X17 12 2940")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
