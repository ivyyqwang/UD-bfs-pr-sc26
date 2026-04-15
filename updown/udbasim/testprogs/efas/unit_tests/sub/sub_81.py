from EFA_v2 import *
def sub_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7960298727262041603, 7788288151076747608]
    tran0.writeAction("movir X16 37255")
    tran0.writeAction("slorii X16 X16 12 1383")
    tran0.writeAction("slorii X16 X16 12 2983")
    tran0.writeAction("slorii X16 X16 12 2260")
    tran0.writeAction("slorii X16 X16 12 2557")
    tran0.writeAction("movir X17 27669")
    tran0.writeAction("slorii X17 X17 12 2284")
    tran0.writeAction("slorii X17 X17 12 3885")
    tran0.writeAction("slorii X17 X17 12 1283")
    tran0.writeAction("slorii X17 X17 12 2392")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
