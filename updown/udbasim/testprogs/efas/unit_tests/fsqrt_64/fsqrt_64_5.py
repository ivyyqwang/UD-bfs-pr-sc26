from EFA_v2 import *
def fsqrt_64_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11602382882917930588]
    tran0.writeAction("movir X16 41219")
    tran0.writeAction("slorii X16 X16 12 3868")
    tran0.writeAction("slorii X16 X16 12 652")
    tran0.writeAction("slorii X16 X16 12 1621")
    tran0.writeAction("slorii X16 X16 12 1628")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
