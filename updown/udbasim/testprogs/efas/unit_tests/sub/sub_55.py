from EFA_v2 import *
def sub_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5168299197760600313, 5120960354337061118]
    tran0.writeAction("movir X16 47174")
    tran0.writeAction("slorii X16 X16 12 2100")
    tran0.writeAction("slorii X16 X16 12 816")
    tran0.writeAction("slorii X16 X16 12 2224")
    tran0.writeAction("slorii X16 X16 12 1799")
    tran0.writeAction("movir X17 18193")
    tran0.writeAction("slorii X17 X17 12 1252")
    tran0.writeAction("slorii X17 X17 12 3949")
    tran0.writeAction("slorii X17 X17 12 487")
    tran0.writeAction("slorii X17 X17 12 2302")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
