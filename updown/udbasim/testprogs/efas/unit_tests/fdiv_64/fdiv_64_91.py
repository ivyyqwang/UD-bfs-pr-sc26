from EFA_v2 import *
def fdiv_64_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8661451781384125638, 13227238996127249964]
    tran0.writeAction("movir X16 30771")
    tran0.writeAction("slorii X16 X16 12 2696")
    tran0.writeAction("slorii X16 X16 12 316")
    tran0.writeAction("slorii X16 X16 12 2355")
    tran0.writeAction("slorii X16 X16 12 3270")
    tran0.writeAction("movir X17 46992")
    tran0.writeAction("slorii X17 X17 12 2428")
    tran0.writeAction("slorii X17 X17 12 2363")
    tran0.writeAction("slorii X17 X17 12 1471")
    tran0.writeAction("slorii X17 X17 12 1580")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
