from EFA_v2 import *
def mul_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3944461588263611305, 6381323481960935932]
    tran0.writeAction("movir X16 51522")
    tran0.writeAction("slorii X16 X16 12 1873")
    tran0.writeAction("slorii X16 X16 12 1417")
    tran0.writeAction("slorii X16 X16 12 1533")
    tran0.writeAction("slorii X16 X16 12 1111")
    tran0.writeAction("movir X17 22671")
    tran0.writeAction("slorii X17 X17 12 62")
    tran0.writeAction("slorii X17 X17 12 1451")
    tran0.writeAction("slorii X17 X17 12 575")
    tran0.writeAction("slorii X17 X17 12 508")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
