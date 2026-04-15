from EFA_v2 import *
def fdiv_64_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13955744808358121816, 4773023280204687441]
    tran0.writeAction("movir X16 49580")
    tran0.writeAction("slorii X16 X16 12 3135")
    tran0.writeAction("slorii X16 X16 12 1638")
    tran0.writeAction("slorii X16 X16 12 769")
    tran0.writeAction("slorii X16 X16 12 344")
    tran0.writeAction("movir X17 16957")
    tran0.writeAction("slorii X17 X17 12 758")
    tran0.writeAction("slorii X17 X17 12 641")
    tran0.writeAction("slorii X17 X17 12 1106")
    tran0.writeAction("slorii X17 X17 12 2129")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
