from EFA_v2 import *
def mul_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7763692405219623364, 6360861268903220744]
    tran0.writeAction("movir X16 27582")
    tran0.writeAction("slorii X16 X16 12 721")
    tran0.writeAction("slorii X16 X16 12 3030")
    tran0.writeAction("slorii X16 X16 12 2104")
    tran0.writeAction("slorii X16 X16 12 452")
    tran0.writeAction("movir X17 22598")
    tran0.writeAction("slorii X17 X17 12 1305")
    tran0.writeAction("slorii X17 X17 12 3950")
    tran0.writeAction("slorii X17 X17 12 2117")
    tran0.writeAction("slorii X17 X17 12 1544")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
