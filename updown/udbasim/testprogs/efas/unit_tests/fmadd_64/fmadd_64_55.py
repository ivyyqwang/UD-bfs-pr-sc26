from EFA_v2 import *
def fmadd_64_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12231576106276048476, 18054728342363228920, 14247042964573298008]
    tran0.writeAction("movir X16 43455")
    tran0.writeAction("slorii X16 X16 12 1178")
    tran0.writeAction("slorii X16 X16 12 2489")
    tran0.writeAction("slorii X16 X16 12 3028")
    tran0.writeAction("slorii X16 X16 12 3676")
    tran0.writeAction("movir X17 64143")
    tran0.writeAction("slorii X17 X17 12 1148")
    tran0.writeAction("slorii X17 X17 12 1266")
    tran0.writeAction("slorii X17 X17 12 3020")
    tran0.writeAction("slorii X17 X17 12 2808")
    tran0.writeAction("movir X18 50615")
    tran0.writeAction("slorii X18 X18 12 2721")
    tran0.writeAction("slorii X18 X18 12 1947")
    tran0.writeAction("slorii X18 X18 12 489")
    tran0.writeAction("slorii X18 X18 12 3416")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
