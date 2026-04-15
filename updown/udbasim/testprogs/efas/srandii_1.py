from EFA_v2 import *
def srandii_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -15219")
    tran0.writeAction("slorii X16 X16 12 1937")
    tran0.writeAction("slorii X16 X16 12 4006")
    tran0.writeAction("slorii X16 X16 12 2831")
    tran0.writeAction("slorii X16 X16 12 2042")
    tran0.writeAction("movir X17 11281")
    tran0.writeAction("slorii X17 X17 12 2195")
    tran0.writeAction("slorii X17 X17 12 1469")
    tran0.writeAction("slorii X17 X17 12 3381")
    tran0.writeAction("slorii X17 X17 12 59")
    tran0.writeAction("srandii X16 X17 12 2015")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
