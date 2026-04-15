from EFA_v2 import *
def sl_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -14794")
    tran0.writeAction("slorii X16 X16 12 2861")
    tran0.writeAction("slorii X16 X16 12 1809")
    tran0.writeAction("slorii X16 X16 12 3315")
    tran0.writeAction("slorii X16 X16 12 2172")
    tran0.writeAction("movir X17 5374")
    tran0.writeAction("slorii X17 X17 12 3246")
    tran0.writeAction("slorii X17 X17 12 2928")
    tran0.writeAction("slorii X17 X17 12 510")
    tran0.writeAction("slorii X17 X17 12 2959")
    tran0.writeAction("movir X18 -5655")
    tran0.writeAction("slorii X18 X18 12 1115")
    tran0.writeAction("slorii X18 X18 12 965")
    tran0.writeAction("slorii X18 X18 12 4092")
    tran0.writeAction("slorii X18 X18 12 4012")
    tran0.writeAction("sl X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
