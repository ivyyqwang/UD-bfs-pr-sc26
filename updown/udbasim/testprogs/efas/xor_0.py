from EFA_v2 import *
def xor_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 28282")
    tran0.writeAction("slorii X16 X16 12 2007")
    tran0.writeAction("slorii X16 X16 12 2068")
    tran0.writeAction("slorii X16 X16 12 3464")
    tran0.writeAction("slorii X16 X16 12 1066")
    tran0.writeAction("movir X17 23465")
    tran0.writeAction("slorii X17 X17 12 2761")
    tran0.writeAction("slorii X17 X17 12 3028")
    tran0.writeAction("slorii X17 X17 12 25")
    tran0.writeAction("slorii X17 X17 12 1202")
    tran0.writeAction("movir X18 31788")
    tran0.writeAction("slorii X18 X18 12 126")
    tran0.writeAction("slorii X18 X18 12 2441")
    tran0.writeAction("slorii X18 X18 12 1565")
    tran0.writeAction("slorii X18 X18 12 3675")
    tran0.writeAction("xor X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
