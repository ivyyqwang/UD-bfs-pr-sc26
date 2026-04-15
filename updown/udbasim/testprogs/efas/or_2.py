from EFA_v2 import *
def or_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 26594")
    tran0.writeAction("slorii X16 X16 12 1383")
    tran0.writeAction("slorii X16 X16 12 243")
    tran0.writeAction("slorii X16 X16 12 1115")
    tran0.writeAction("slorii X16 X16 12 1267")
    tran0.writeAction("movir X17 -22712")
    tran0.writeAction("slorii X17 X17 12 1087")
    tran0.writeAction("slorii X17 X17 12 1503")
    tran0.writeAction("slorii X17 X17 12 3130")
    tran0.writeAction("slorii X17 X17 12 234")
    tran0.writeAction("movir X18 -29405")
    tran0.writeAction("slorii X18 X18 12 664")
    tran0.writeAction("slorii X18 X18 12 195")
    tran0.writeAction("slorii X18 X18 12 3156")
    tran0.writeAction("slorii X18 X18 12 3333")
    tran0.writeAction("or X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
