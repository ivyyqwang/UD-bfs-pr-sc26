from EFA_v2 import *
def fsqrt_64_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16803446670706745106]
    tran0.writeAction("movir X16 59697")
    tran0.writeAction("slorii X16 X16 12 3419")
    tran0.writeAction("slorii X16 X16 12 2033")
    tran0.writeAction("slorii X16 X16 12 2849")
    tran0.writeAction("slorii X16 X16 12 3858")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
