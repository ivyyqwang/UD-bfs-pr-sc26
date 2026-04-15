from EFA_v2 import *
def sl_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 31834")
    tran0.writeAction("slorii X16 X16 12 3197")
    tran0.writeAction("slorii X16 X16 12 2625")
    tran0.writeAction("slorii X16 X16 12 2469")
    tran0.writeAction("slorii X16 X16 12 3728")
    tran0.writeAction("movir X17 -11364")
    tran0.writeAction("slorii X17 X17 12 3085")
    tran0.writeAction("slorii X17 X17 12 1367")
    tran0.writeAction("slorii X17 X17 12 2735")
    tran0.writeAction("slorii X17 X17 12 1959")
    tran0.writeAction("movir X18 5825")
    tran0.writeAction("slorii X18 X18 12 1764")
    tran0.writeAction("slorii X18 X18 12 2492")
    tran0.writeAction("slorii X18 X18 12 195")
    tran0.writeAction("slorii X18 X18 12 2669")
    tran0.writeAction("sl X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
