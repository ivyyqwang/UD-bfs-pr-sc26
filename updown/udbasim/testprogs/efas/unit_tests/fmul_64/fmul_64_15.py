from EFA_v2 import *
def fmul_64_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11480024253230734370, 10708398962692162981]
    tran0.writeAction("movir X16 40785")
    tran0.writeAction("slorii X16 X16 12 979")
    tran0.writeAction("slorii X16 X16 12 3082")
    tran0.writeAction("slorii X16 X16 12 2813")
    tran0.writeAction("slorii X16 X16 12 3106")
    tran0.writeAction("movir X17 38043")
    tran0.writeAction("slorii X17 X17 12 3585")
    tran0.writeAction("slorii X17 X17 12 3836")
    tran0.writeAction("slorii X17 X17 12 1752")
    tran0.writeAction("slorii X17 X17 12 1445")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
