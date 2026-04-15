from EFA_v2 import *
def fmadd_64_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17604742826193467732, 16093400275885204090, 10945912248087906778]
    tran0.writeAction("movir X16 62544")
    tran0.writeAction("slorii X16 X16 12 2501")
    tran0.writeAction("slorii X16 X16 12 917")
    tran0.writeAction("slorii X16 X16 12 1507")
    tran0.writeAction("slorii X16 X16 12 2388")
    tran0.writeAction("movir X17 57175")
    tran0.writeAction("slorii X17 X17 12 996")
    tran0.writeAction("slorii X17 X17 12 2256")
    tran0.writeAction("slorii X17 X17 12 1274")
    tran0.writeAction("slorii X17 X17 12 634")
    tran0.writeAction("movir X18 38887")
    tran0.writeAction("slorii X18 X18 12 2835")
    tran0.writeAction("slorii X18 X18 12 537")
    tran0.writeAction("slorii X18 X18 12 3592")
    tran0.writeAction("slorii X18 X18 12 2522")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
