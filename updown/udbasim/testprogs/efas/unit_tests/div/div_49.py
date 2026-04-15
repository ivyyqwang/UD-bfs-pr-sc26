from EFA_v2 import *
def div_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6638124348521555856, 7304869113794882965]
    tran0.writeAction("movir X16 23583")
    tran0.writeAction("slorii X16 X16 12 1454")
    tran0.writeAction("slorii X16 X16 12 3256")
    tran0.writeAction("slorii X16 X16 12 2042")
    tran0.writeAction("slorii X16 X16 12 1936")
    tran0.writeAction("movir X17 25952")
    tran0.writeAction("slorii X17 X17 12 444")
    tran0.writeAction("slorii X17 X17 12 402")
    tran0.writeAction("slorii X17 X17 12 1910")
    tran0.writeAction("slorii X17 X17 12 3477")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
