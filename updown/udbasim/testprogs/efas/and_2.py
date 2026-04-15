from EFA_v2 import *
def and_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -16711")
    tran0.writeAction("slorii X16 X16 12 1828")
    tran0.writeAction("slorii X16 X16 12 1286")
    tran0.writeAction("slorii X16 X16 12 784")
    tran0.writeAction("slorii X16 X16 12 518")
    tran0.writeAction("movir X17 -21013")
    tran0.writeAction("slorii X17 X17 12 3032")
    tran0.writeAction("slorii X17 X17 12 3369")
    tran0.writeAction("slorii X17 X17 12 1231")
    tran0.writeAction("slorii X17 X17 12 2115")
    tran0.writeAction("movir X18 -31273")
    tran0.writeAction("slorii X18 X18 12 535")
    tran0.writeAction("slorii X18 X18 12 739")
    tran0.writeAction("slorii X18 X18 12 699")
    tran0.writeAction("slorii X18 X18 12 2988")
    tran0.writeAction("and X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
