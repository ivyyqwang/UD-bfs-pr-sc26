from EFA_v2 import *
def xor_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 -7824")
    tran0.writeAction("slorii X16 X16 12 2514")
    tran0.writeAction("slorii X16 X16 12 3624")
    tran0.writeAction("slorii X16 X16 12 722")
    tran0.writeAction("slorii X16 X16 12 1782")
    tran0.writeAction("movir X17 20408")
    tran0.writeAction("slorii X17 X17 12 78")
    tran0.writeAction("slorii X17 X17 12 1837")
    tran0.writeAction("slorii X17 X17 12 1382")
    tran0.writeAction("slorii X17 X17 12 2155")
    tran0.writeAction("movir X18 12407")
    tran0.writeAction("slorii X18 X18 12 3635")
    tran0.writeAction("slorii X18 X18 12 2917")
    tran0.writeAction("slorii X18 X18 12 4024")
    tran0.writeAction("slorii X18 X18 12 437")
    tran0.writeAction("xor X16 X17 X18")
    tran0.writeAction(f"print '%d,%d,%d' X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
