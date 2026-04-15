from EFA_v2 import *
def fsqrt_64_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16498076340294539982]
    tran0.writeAction("movir X16 58612")
    tran0.writeAction("slorii X16 X16 12 3856")
    tran0.writeAction("slorii X16 X16 12 1372")
    tran0.writeAction("slorii X16 X16 12 2181")
    tran0.writeAction("slorii X16 X16 12 2766")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
