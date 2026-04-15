from EFA_v2 import *
def fmul_64_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13246774072774026107, 9199956295362997666]
    tran0.writeAction("movir X16 47061")
    tran0.writeAction("slorii X16 X16 12 4077")
    tran0.writeAction("slorii X16 X16 12 1459")
    tran0.writeAction("slorii X16 X16 12 2254")
    tran0.writeAction("slorii X16 X16 12 891")
    tran0.writeAction("movir X17 32684")
    tran0.writeAction("slorii X17 X17 12 3320")
    tran0.writeAction("slorii X17 X17 12 470")
    tran0.writeAction("slorii X17 X17 12 942")
    tran0.writeAction("slorii X17 X17 12 3490")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
