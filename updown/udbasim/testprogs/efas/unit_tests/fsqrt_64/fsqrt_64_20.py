from EFA_v2 import *
def fsqrt_64_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4796306320766374744]
    tran0.writeAction("movir X16 17039")
    tran0.writeAction("slorii X16 X16 12 3698")
    tran0.writeAction("slorii X16 X16 12 4051")
    tran0.writeAction("slorii X16 X16 12 985")
    tran0.writeAction("slorii X16 X16 12 856")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
