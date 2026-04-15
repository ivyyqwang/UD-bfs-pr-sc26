from EFA_v2 import *
def fadd_64_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18063403576202662915, 1857137189108784958]
    tran0.writeAction("movir X16 64174")
    tran0.writeAction("slorii X16 X16 12 413")
    tran0.writeAction("slorii X16 X16 12 2362")
    tran0.writeAction("slorii X16 X16 12 329")
    tran0.writeAction("slorii X16 X16 12 1027")
    tran0.writeAction("movir X17 6597")
    tran0.writeAction("slorii X17 X17 12 3590")
    tran0.writeAction("slorii X17 X17 12 3863")
    tran0.writeAction("slorii X17 X17 12 4081")
    tran0.writeAction("slorii X17 X17 12 3902")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
