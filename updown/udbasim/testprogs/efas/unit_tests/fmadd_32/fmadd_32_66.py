from EFA_v2 import *
def fmadd_32_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2400818384, 922542183, 1228204408]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 143")
    tran0.writeAction("slorii X16 X16 12 409")
    tran0.writeAction("slorii X16 X16 12 1232")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 54")
    tran0.writeAction("slorii X17 X17 12 4046")
    tran0.writeAction("slorii X17 X17 12 103")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 73")
    tran0.writeAction("slorii X18 X18 12 846")
    tran0.writeAction("slorii X18 X18 12 2424")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
