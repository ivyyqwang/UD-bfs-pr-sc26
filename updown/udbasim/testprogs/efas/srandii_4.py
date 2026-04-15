from EFA_v2 import *
def srandii_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 21352")
    tran0.writeAction("slorii X16 X16 12 3765")
    tran0.writeAction("slorii X16 X16 12 958")
    tran0.writeAction("slorii X16 X16 12 281")
    tran0.writeAction("slorii X16 X16 12 3355")
    tran0.writeAction("movir X17 -8298")
    tran0.writeAction("slorii X17 X17 12 377")
    tran0.writeAction("slorii X17 X17 12 531")
    tran0.writeAction("slorii X17 X17 12 1635")
    tran0.writeAction("slorii X17 X17 12 4004")
    tran0.writeAction("srandii X16 X17 9 2061")
    tran0.writeAction(f"print '%d,%d' X16 X17")
    tran0.writeAction("yieldt")
    return efa
