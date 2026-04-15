from EFA_v2 import *
def sari_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -17020")
    tran0.writeAction("slorii X16 X16 12 224")
    tran0.writeAction("slorii X16 X16 12 1667")
    tran0.writeAction("slorii X16 X16 12 2343")
    tran0.writeAction("slorii X16 X16 12 2889")
    tran0.writeAction("movir X17 -4981")
    tran0.writeAction("slorii X17 X17 12 2017")
    tran0.writeAction("slorii X17 X17 12 3299")
    tran0.writeAction("slorii X17 X17 12 3481")
    tran0.writeAction("slorii X17 X17 12 37")
    tran0.writeAction("sari X16 X17 11")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
