from EFA_v2 import *
def fsqrt_64_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [845264691237243416]
    tran0.writeAction("movir X16 3002")
    tran0.writeAction("slorii X16 X16 12 4028")
    tran0.writeAction("slorii X16 X16 12 542")
    tran0.writeAction("slorii X16 X16 12 1540")
    tran0.writeAction("slorii X16 X16 12 2584")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
