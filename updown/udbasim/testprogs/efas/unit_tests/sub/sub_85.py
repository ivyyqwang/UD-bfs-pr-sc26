from EFA_v2 import *
def sub_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2149208500380625227, 313299805837626286]
    tran0.writeAction("movir X16 57900")
    tran0.writeAction("slorii X16 X16 12 1956")
    tran0.writeAction("slorii X16 X16 12 386")
    tran0.writeAction("slorii X16 X16 12 2305")
    tran0.writeAction("slorii X16 X16 12 1717")
    tran0.writeAction("movir X17 1113")
    tran0.writeAction("slorii X17 X17 12 264")
    tran0.writeAction("slorii X17 X17 12 883")
    tran0.writeAction("slorii X17 X17 12 616")
    tran0.writeAction("slorii X17 X17 12 2990")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
