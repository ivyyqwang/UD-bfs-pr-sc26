from EFA_v2 import *
def fsqrt_64_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4314029700427486038]
    tran0.writeAction("movir X16 15326")
    tran0.writeAction("slorii X16 X16 12 2098")
    tran0.writeAction("slorii X16 X16 12 2020")
    tran0.writeAction("slorii X16 X16 12 1905")
    tran0.writeAction("slorii X16 X16 12 854")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
