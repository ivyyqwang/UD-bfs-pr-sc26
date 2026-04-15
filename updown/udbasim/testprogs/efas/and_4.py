from EFA_v2 import *
def and_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -32485")
    tran0.writeAction("slorii X16 X16 12 1510")
    tran0.writeAction("slorii X16 X16 12 3859")
    tran0.writeAction("slorii X16 X16 12 3901")
    tran0.writeAction("slorii X16 X16 12 485")
    tran0.writeAction("movir X17 -2387")
    tran0.writeAction("slorii X17 X17 12 1006")
    tran0.writeAction("slorii X17 X17 12 571")
    tran0.writeAction("slorii X17 X17 12 1415")
    tran0.writeAction("slorii X17 X17 12 3580")
    tran0.writeAction("movir X18 -23327")
    tran0.writeAction("slorii X18 X18 12 1785")
    tran0.writeAction("slorii X18 X18 12 1315")
    tran0.writeAction("slorii X18 X18 12 2528")
    tran0.writeAction("slorii X18 X18 12 2896")
    tran0.writeAction("and X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
