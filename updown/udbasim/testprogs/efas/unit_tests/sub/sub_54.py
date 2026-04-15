from EFA_v2 import *
def sub_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [879913535676677682, -1352419507008680803]
    tran0.writeAction("movir X16 3126")
    tran0.writeAction("slorii X16 X16 12 331")
    tran0.writeAction("slorii X16 X16 12 735")
    tran0.writeAction("slorii X16 X16 12 271")
    tran0.writeAction("slorii X16 X16 12 3634")
    tran0.writeAction("movir X17 60731")
    tran0.writeAction("slorii X17 X17 12 985")
    tran0.writeAction("slorii X17 X17 12 4017")
    tran0.writeAction("slorii X17 X17 12 1796")
    tran0.writeAction("slorii X17 X17 12 3229")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
