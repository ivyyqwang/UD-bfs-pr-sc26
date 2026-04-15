from EFA_v2 import *
def fsub_64_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16647212756611602513, 6401767084332253341]
    tran0.writeAction("movir X16 59142")
    tran0.writeAction("slorii X16 X16 12 3196")
    tran0.writeAction("slorii X16 X16 12 3370")
    tran0.writeAction("slorii X16 X16 12 761")
    tran0.writeAction("slorii X16 X16 12 2129")
    tran0.writeAction("movir X17 22743")
    tran0.writeAction("slorii X17 X17 12 2643")
    tran0.writeAction("slorii X17 X17 12 3780")
    tran0.writeAction("slorii X17 X17 12 1688")
    tran0.writeAction("slorii X17 X17 12 157")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
