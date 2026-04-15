from EFA_v2 import *
def fsqrt_64_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6818298782691753520]
    tran0.writeAction("movir X16 24223")
    tran0.writeAction("slorii X16 X16 12 1897")
    tran0.writeAction("slorii X16 X16 12 3634")
    tran0.writeAction("slorii X16 X16 12 3359")
    tran0.writeAction("slorii X16 X16 12 3632")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
