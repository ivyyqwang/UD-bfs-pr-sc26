from EFA_v2 import *
def sari_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -17413")
    tran0.writeAction("slorii X16 X16 12 1386")
    tran0.writeAction("slorii X16 X16 12 2855")
    tran0.writeAction("slorii X16 X16 12 559")
    tran0.writeAction("slorii X16 X16 12 1132")
    tran0.writeAction("movir X17 -17452")
    tran0.writeAction("slorii X17 X17 12 1539")
    tran0.writeAction("slorii X17 X17 12 3205")
    tran0.writeAction("slorii X17 X17 12 2172")
    tran0.writeAction("slorii X17 X17 12 328")
    tran0.writeAction("sari X16 X17 51")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
