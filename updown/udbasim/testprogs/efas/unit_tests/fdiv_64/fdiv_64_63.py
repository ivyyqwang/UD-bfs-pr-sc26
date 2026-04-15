from EFA_v2 import *
def fdiv_64_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14648423618197661557, 17447262536368939902]
    tran0.writeAction("movir X16 52041")
    tran0.writeAction("slorii X16 X16 12 2682")
    tran0.writeAction("slorii X16 X16 12 2954")
    tran0.writeAction("slorii X16 X16 12 466")
    tran0.writeAction("slorii X16 X16 12 1909")
    tran0.writeAction("movir X17 61985")
    tran0.writeAction("slorii X17 X17 12 525")
    tran0.writeAction("slorii X17 X17 12 1623")
    tran0.writeAction("slorii X17 X17 12 1030")
    tran0.writeAction("slorii X17 X17 12 894")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
