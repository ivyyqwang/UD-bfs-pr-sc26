from EFA_v2 import *
def fdiv_64_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2715704005970582598, 3922822474444156442]
    tran0.writeAction("movir X16 9648")
    tran0.writeAction("slorii X16 X16 12 486")
    tran0.writeAction("slorii X16 X16 12 1966")
    tran0.writeAction("slorii X16 X16 12 4021")
    tran0.writeAction("slorii X16 X16 12 3142")
    tran0.writeAction("movir X17 13936")
    tran0.writeAction("slorii X17 X17 12 2724")
    tran0.writeAction("slorii X17 X17 12 426")
    tran0.writeAction("slorii X17 X17 12 666")
    tran0.writeAction("slorii X17 X17 12 3610")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
