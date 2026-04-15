from EFA_v2 import *
def fcnvt_64_b16_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [63203959257111054]
    tran0.writeAction("movir X16 224")
    tran0.writeAction("slorii X16 X16 12 2234")
    tran0.writeAction("slorii X16 X16 12 2691")
    tran0.writeAction("slorii X16 X16 12 3761")
    tran0.writeAction("slorii X16 X16 12 2574")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
