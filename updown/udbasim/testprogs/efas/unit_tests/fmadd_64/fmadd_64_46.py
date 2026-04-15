from EFA_v2 import *
def fmadd_64_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7999387178134700861, 17810173553282656650, 6572294761911658152]
    tran0.writeAction("movir X16 28419")
    tran0.writeAction("slorii X16 X16 12 2180")
    tran0.writeAction("slorii X16 X16 12 389")
    tran0.writeAction("slorii X16 X16 12 2184")
    tran0.writeAction("slorii X16 X16 12 829")
    tran0.writeAction("movir X17 63274")
    tran0.writeAction("slorii X17 X17 12 1831")
    tran0.writeAction("slorii X17 X17 12 3071")
    tran0.writeAction("slorii X17 X17 12 1922")
    tran0.writeAction("slorii X17 X17 12 2442")
    tran0.writeAction("movir X18 23349")
    tran0.writeAction("slorii X18 X18 12 1972")
    tran0.writeAction("slorii X18 X18 12 946")
    tran0.writeAction("slorii X18 X18 12 3706")
    tran0.writeAction("slorii X18 X18 12 1704")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
