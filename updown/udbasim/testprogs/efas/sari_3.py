from EFA_v2 import *
def sari_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 25356")
    tran0.writeAction("slorii X16 X16 12 1865")
    tran0.writeAction("slorii X16 X16 12 1707")
    tran0.writeAction("slorii X16 X16 12 557")
    tran0.writeAction("slorii X16 X16 12 3492")
    tran0.writeAction("movir X17 19404")
    tran0.writeAction("slorii X17 X17 12 3841")
    tran0.writeAction("slorii X17 X17 12 1362")
    tran0.writeAction("slorii X17 X17 12 1410")
    tran0.writeAction("slorii X17 X17 12 1696")
    tran0.writeAction("sari X16 X17 47")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
