from EFA_v2 import *
def srandi_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 1193")
    tran0.writeAction("slorii X16 X16 12 2142")
    tran0.writeAction("slorii X16 X16 12 2953")
    tran0.writeAction("slorii X16 X16 12 4095")
    tran0.writeAction("slorii X16 X16 12 3688")
    tran0.writeAction("movir X17 -9430")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 1345")
    tran0.writeAction("slorii X17 X17 12 2745")
    tran0.writeAction("slorii X17 X17 12 3442")
    tran0.writeAction("srandi X16 X17 54")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
