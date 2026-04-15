from EFA_v2 import *
def fdiv_64_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12913546659336518610, 5822781593917391878]
    tran0.writeAction("movir X16 45878")
    tran0.writeAction("slorii X16 X16 12 548")
    tran0.writeAction("slorii X16 X16 12 1164")
    tran0.writeAction("slorii X16 X16 12 759")
    tran0.writeAction("slorii X16 X16 12 3026")
    tran0.writeAction("movir X17 20686")
    tran0.writeAction("slorii X17 X17 12 2768")
    tran0.writeAction("slorii X17 X17 12 606")
    tran0.writeAction("slorii X17 X17 12 528")
    tran0.writeAction("slorii X17 X17 12 1030")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
