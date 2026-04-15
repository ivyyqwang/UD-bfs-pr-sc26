from EFA_v2 import *
def srandii_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -19678")
    tran0.writeAction("slorii X16 X16 12 976")
    tran0.writeAction("slorii X16 X16 12 965")
    tran0.writeAction("slorii X16 X16 12 938")
    tran0.writeAction("slorii X16 X16 12 2090")
    tran0.writeAction("movir X17 -24389")
    tran0.writeAction("slorii X17 X17 12 1525")
    tran0.writeAction("slorii X17 X17 12 812")
    tran0.writeAction("slorii X17 X17 12 3110")
    tran0.writeAction("slorii X17 X17 12 4046")
    tran0.writeAction("srandii X16 X17 13 643")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
