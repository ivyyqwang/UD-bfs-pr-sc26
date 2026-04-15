from EFA_v2 import *
def sri_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -20776")
    tran0.writeAction("slorii X16 X16 12 2831")
    tran0.writeAction("slorii X16 X16 12 1095")
    tran0.writeAction("slorii X16 X16 12 913")
    tran0.writeAction("slorii X16 X16 12 3805")
    tran0.writeAction("movir X17 26559")
    tran0.writeAction("slorii X17 X17 12 1618")
    tran0.writeAction("slorii X17 X17 12 2776")
    tran0.writeAction("slorii X17 X17 12 123")
    tran0.writeAction("slorii X17 X17 12 3240")
    tran0.writeAction("sri X16 X17 46")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
