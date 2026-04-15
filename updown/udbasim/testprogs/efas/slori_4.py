from EFA_v2 import *
def slori_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 10695")
    tran0.writeAction("slorii X16 X16 12 3370")
    tran0.writeAction("slorii X16 X16 12 584")
    tran0.writeAction("slorii X16 X16 12 3876")
    tran0.writeAction("slorii X16 X16 12 2855")
    tran0.writeAction("movir X17 19727")
    tran0.writeAction("slorii X17 X17 12 2886")
    tran0.writeAction("slorii X17 X17 12 1094")
    tran0.writeAction("slorii X17 X17 12 1164")
    tran0.writeAction("slorii X17 X17 12 1884")
    tran0.writeAction("slori X16 X17 61")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
