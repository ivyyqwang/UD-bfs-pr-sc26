from EFA_v2 import *
def xor_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -4255")
    tran0.writeAction("slorii X16 X16 12 3602")
    tran0.writeAction("slorii X16 X16 12 65")
    tran0.writeAction("slorii X16 X16 12 2493")
    tran0.writeAction("slorii X16 X16 12 1226")
    tran0.writeAction("movir X17 9436")
    tran0.writeAction("slorii X17 X17 12 1799")
    tran0.writeAction("slorii X17 X17 12 1514")
    tran0.writeAction("slorii X17 X17 12 3056")
    tran0.writeAction("slorii X17 X17 12 3756")
    tran0.writeAction("movir X18 21334")
    tran0.writeAction("slorii X18 X18 12 298")
    tran0.writeAction("slorii X18 X18 12 3034")
    tran0.writeAction("slorii X18 X18 12 3315")
    tran0.writeAction("slorii X18 X18 12 1481")
    tran0.writeAction("xor X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
