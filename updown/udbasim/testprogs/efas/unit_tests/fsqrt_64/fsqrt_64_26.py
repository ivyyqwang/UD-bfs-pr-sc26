from EFA_v2 import *
def fsqrt_64_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18412534903938573796]
    tran0.writeAction("movir X16 65414")
    tran0.writeAction("slorii X16 X16 12 1903")
    tran0.writeAction("slorii X16 X16 12 251")
    tran0.writeAction("slorii X16 X16 12 3030")
    tran0.writeAction("slorii X16 X16 12 1508")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
