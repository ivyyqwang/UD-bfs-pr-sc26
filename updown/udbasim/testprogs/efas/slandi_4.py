from EFA_v2 import *
def slandi_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 2953")
    tran0.writeAction("slorii X16 X16 12 3028")
    tran0.writeAction("slorii X16 X16 12 3601")
    tran0.writeAction("slorii X16 X16 12 205")
    tran0.writeAction("slorii X16 X16 12 3562")
    tran0.writeAction("movir X17 -23322")
    tran0.writeAction("slorii X17 X17 12 358")
    tran0.writeAction("slorii X17 X17 12 1998")
    tran0.writeAction("slorii X17 X17 12 3957")
    tran0.writeAction("slorii X17 X17 12 1411")
    tran0.writeAction("slandi X16 X17 39")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
