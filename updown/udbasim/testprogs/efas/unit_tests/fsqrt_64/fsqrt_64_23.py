from EFA_v2 import *
def fsqrt_64_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14689903768218099078]
    tran0.writeAction("movir X16 52189")
    tran0.writeAction("slorii X16 X16 12 90")
    tran0.writeAction("slorii X16 X16 12 1425")
    tran0.writeAction("slorii X16 X16 12 1277")
    tran0.writeAction("slorii X16 X16 12 3462")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
