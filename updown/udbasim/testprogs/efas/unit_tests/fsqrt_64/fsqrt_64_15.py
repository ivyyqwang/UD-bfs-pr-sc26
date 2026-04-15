from EFA_v2 import *
def fsqrt_64_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9434959113071926680]
    tran0.writeAction("movir X16 33519")
    tran0.writeAction("slorii X16 X16 12 2901")
    tran0.writeAction("slorii X16 X16 12 804")
    tran0.writeAction("slorii X16 X16 12 4041")
    tran0.writeAction("slorii X16 X16 12 3480")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
