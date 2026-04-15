from EFA_v2 import *
def fsqrt_64_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13099804768034836127]
    tran0.writeAction("movir X16 46539")
    tran0.writeAction("slorii X16 X16 12 3504")
    tran0.writeAction("slorii X16 X16 12 2017")
    tran0.writeAction("slorii X16 X16 12 2804")
    tran0.writeAction("slorii X16 X16 12 3743")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
