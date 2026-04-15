from EFA_v2 import *
def fdiv_64_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [819593318266269356, 7872199561699623125]
    tran0.writeAction("movir X16 2911")
    tran0.writeAction("slorii X16 X16 12 3196")
    tran0.writeAction("slorii X16 X16 12 2003")
    tran0.writeAction("slorii X16 X16 12 2230")
    tran0.writeAction("slorii X16 X16 12 3756")
    tran0.writeAction("movir X17 27967")
    tran0.writeAction("slorii X17 X17 12 2748")
    tran0.writeAction("slorii X17 X17 12 2796")
    tran0.writeAction("slorii X17 X17 12 376")
    tran0.writeAction("slorii X17 X17 12 213")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
