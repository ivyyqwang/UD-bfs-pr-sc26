from EFA_v2 import *
def fadd_64_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4274493319868020676, 3349878034452561652]
    tran0.writeAction("movir X16 15186")
    tran0.writeAction("slorii X16 X16 12 208")
    tran0.writeAction("slorii X16 X16 12 1781")
    tran0.writeAction("slorii X16 X16 12 2103")
    tran0.writeAction("slorii X16 X16 12 1988")
    tran0.writeAction("movir X17 11901")
    tran0.writeAction("slorii X17 X17 12 645")
    tran0.writeAction("slorii X17 X17 12 748")
    tran0.writeAction("slorii X17 X17 12 1755")
    tran0.writeAction("slorii X17 X17 12 3828")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
