from EFA_v2 import *
def divi_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2189631231002563341, -16442]
    tran0.writeAction("movir X16 57756")
    tran0.writeAction("slorii X16 X16 12 3551")
    tran0.writeAction("slorii X16 X16 12 3870")
    tran0.writeAction("slorii X16 X16 12 4058")
    tran0.writeAction("slorii X16 X16 12 3315")
    tran0.writeAction("divi X16 X17 -16442")
    tran0.writeAction("yieldt")
    return efa
