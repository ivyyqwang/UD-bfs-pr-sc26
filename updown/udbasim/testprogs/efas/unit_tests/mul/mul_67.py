from EFA_v2 import *
def mul_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4853715484831184268, -4344791566427062517]
    tran0.writeAction("movir X16 48292")
    tran0.writeAction("slorii X16 X16 12 567")
    tran0.writeAction("slorii X16 X16 12 2957")
    tran0.writeAction("slorii X16 X16 12 3376")
    tran0.writeAction("slorii X16 X16 12 2676")
    tran0.writeAction("movir X17 50100")
    tran0.writeAction("slorii X17 X17 12 817")
    tran0.writeAction("slorii X17 X17 12 1804")
    tran0.writeAction("slorii X17 X17 12 7")
    tran0.writeAction("slorii X17 X17 12 3851")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
