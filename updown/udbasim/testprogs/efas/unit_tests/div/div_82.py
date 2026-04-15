from EFA_v2 import *
def div_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5163596759719363325, -3455768310333244438]
    tran0.writeAction("movir X16 18344")
    tran0.writeAction("slorii X16 X16 12 3198")
    tran0.writeAction("slorii X16 X16 12 1314")
    tran0.writeAction("slorii X16 X16 12 1764")
    tran0.writeAction("slorii X16 X16 12 765")
    tran0.writeAction("movir X17 53258")
    tran0.writeAction("slorii X17 X17 12 2640")
    tran0.writeAction("slorii X17 X17 12 2044")
    tran0.writeAction("slorii X17 X17 12 2191")
    tran0.writeAction("slorii X17 X17 12 3050")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
