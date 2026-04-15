from EFA_v2 import *
def fsqrt_64_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15150960668679877530]
    tran0.writeAction("movir X16 53827")
    tran0.writeAction("slorii X16 X16 12 103")
    tran0.writeAction("slorii X16 X16 12 1142")
    tran0.writeAction("slorii X16 X16 12 2371")
    tran0.writeAction("slorii X16 X16 12 922")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
