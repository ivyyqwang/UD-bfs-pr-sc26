from EFA_v2 import *
def xor_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -12207")
    tran0.writeAction("slorii X16 X16 12 3691")
    tran0.writeAction("slorii X16 X16 12 1910")
    tran0.writeAction("slorii X16 X16 12 2681")
    tran0.writeAction("slorii X16 X16 12 3936")
    tran0.writeAction("movir X17 24767")
    tran0.writeAction("slorii X17 X17 12 2630")
    tran0.writeAction("slorii X17 X17 12 3558")
    tran0.writeAction("slorii X17 X17 12 3557")
    tran0.writeAction("slorii X17 X17 12 2711")
    tran0.writeAction("movir X18 2864")
    tran0.writeAction("slorii X18 X18 12 3214")
    tran0.writeAction("slorii X18 X18 12 1946")
    tran0.writeAction("slorii X18 X18 12 2844")
    tran0.writeAction("slorii X18 X18 12 1402")
    tran0.writeAction("xor X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
