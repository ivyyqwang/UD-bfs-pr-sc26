from EFA_v2 import *
def add_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9132425051644550302, -1547519360270088337]
    tran0.writeAction("movir X16 33091")
    tran0.writeAction("slorii X16 X16 12 444")
    tran0.writeAction("slorii X16 X16 12 3354")
    tran0.writeAction("slorii X16 X16 12 3474")
    tran0.writeAction("slorii X16 X16 12 866")
    tran0.writeAction("movir X17 60038")
    tran0.writeAction("slorii X17 X17 12 437")
    tran0.writeAction("slorii X17 X17 12 1864")
    tran0.writeAction("slorii X17 X17 12 252")
    tran0.writeAction("slorii X17 X17 12 1903")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
