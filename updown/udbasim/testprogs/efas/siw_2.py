from EFA_v2 import *
def siw_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 60111")
    tran0.writeAction("slorii X16 X16 12 1685")
    tran0.writeAction("slorii X16 X16 12 1310")
    tran0.writeAction("slorii X16 X16 12 1378")
    tran0.writeAction("slorii X16 X16 12 3024")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("add X7 X17 X17")
    tran0.writeAction("movrl X16 0(X17) 0 8")
    tran0.writeAction("movir X18 1")
    tran0.writeAction("sli X18 X18 23")
    tran0.writeAction("or X18 X2 X2")
    tran0.writeAction("sri X16 X16 40")
    tran0.writeAction("sli X16 X16 40")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("sli X17 X17 40")
    tran0.writeAction("or X17 X16 X16")
    tran0.writeAction("movir X17 1")
    tran0.writeAction("sli X17 X17 32")
    tran0.writeAction("or X17 X16 X16")
    tran0.writeAction("movir X17 512")
    tran0.writeAction("or X17 X16 X4")
    tran0.writeAction("movrr X4 X18")
    tran0.writeAction("siw 3")
    tran0.writeAction("yieldt")
    return efa
