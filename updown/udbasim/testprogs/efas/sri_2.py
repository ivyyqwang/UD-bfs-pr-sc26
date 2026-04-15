from EFA_v2 import *
def sri_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 19978")
    tran0.writeAction("slorii X16 X16 12 1037")
    tran0.writeAction("slorii X16 X16 12 4022")
    tran0.writeAction("slorii X16 X16 12 2114")
    tran0.writeAction("slorii X16 X16 12 880")
    tran0.writeAction("movir X17 -8277")
    tran0.writeAction("slorii X17 X17 12 1590")
    tran0.writeAction("slorii X17 X17 12 2256")
    tran0.writeAction("slorii X17 X17 12 3347")
    tran0.writeAction("slorii X17 X17 12 1766")
    tran0.writeAction("sri X16 X17 28")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
