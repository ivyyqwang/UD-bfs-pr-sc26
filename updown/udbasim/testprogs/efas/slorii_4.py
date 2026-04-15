from EFA_v2 import *
def slorii_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -15505")
    tran0.writeAction("slorii X16 X16 12 1298")
    tran0.writeAction("slorii X16 X16 12 3933")
    tran0.writeAction("slorii X16 X16 12 2123")
    tran0.writeAction("slorii X16 X16 12 3610")
    tran0.writeAction("movir X17 10060")
    tran0.writeAction("slorii X17 X17 12 1771")
    tran0.writeAction("slorii X17 X17 12 3573")
    tran0.writeAction("slorii X17 X17 12 3")
    tran0.writeAction("slorii X17 X17 12 679")
    tran0.writeAction("slorii X16 X17 0 991")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
