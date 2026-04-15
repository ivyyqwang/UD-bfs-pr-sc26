from EFA_v2 import *
def xor_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -28497")
    tran0.writeAction("slorii X16 X16 12 2804")
    tran0.writeAction("slorii X16 X16 12 384")
    tran0.writeAction("slorii X16 X16 12 2291")
    tran0.writeAction("slorii X16 X16 12 3169")
    tran0.writeAction("movir X17 -15210")
    tran0.writeAction("slorii X17 X17 12 935")
    tran0.writeAction("slorii X17 X17 12 3915")
    tran0.writeAction("slorii X17 X17 12 2144")
    tran0.writeAction("slorii X17 X17 12 689")
    tran0.writeAction("movir X18 24167")
    tran0.writeAction("slorii X18 X18 12 438")
    tran0.writeAction("slorii X18 X18 12 938")
    tran0.writeAction("slorii X18 X18 12 2055")
    tran0.writeAction("slorii X18 X18 12 444")
    tran0.writeAction("xor X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
