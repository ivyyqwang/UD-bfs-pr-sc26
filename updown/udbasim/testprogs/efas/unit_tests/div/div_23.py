from EFA_v2 import *
def div_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3209362844296175560, -8121017739076210457]
    tran0.writeAction("movir X16 11401")
    tran0.writeAction("slorii X16 X16 12 3880")
    tran0.writeAction("slorii X16 X16 12 193")
    tran0.writeAction("slorii X16 X16 12 2501")
    tran0.writeAction("slorii X16 X16 12 4040")
    tran0.writeAction("movir X17 36684")
    tran0.writeAction("slorii X17 X17 12 1430")
    tran0.writeAction("slorii X17 X17 12 1199")
    tran0.writeAction("slorii X17 X17 12 2935")
    tran0.writeAction("slorii X17 X17 12 231")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
