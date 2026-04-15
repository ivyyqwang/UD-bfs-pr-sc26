from EFA_v2 import *
def srandii_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -23602")
    tran0.writeAction("slorii X16 X16 12 4000")
    tran0.writeAction("slorii X16 X16 12 2771")
    tran0.writeAction("slorii X16 X16 12 1432")
    tran0.writeAction("slorii X16 X16 12 3364")
    tran0.writeAction("movir X17 -15324")
    tran0.writeAction("slorii X17 X17 12 855")
    tran0.writeAction("slorii X17 X17 12 3221")
    tran0.writeAction("slorii X17 X17 12 249")
    tran0.writeAction("slorii X17 X17 12 3842")
    tran0.writeAction("srandii X16 X17 9 301")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
