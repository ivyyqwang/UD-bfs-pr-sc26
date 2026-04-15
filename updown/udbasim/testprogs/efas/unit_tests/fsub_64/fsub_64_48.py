from EFA_v2 import *
def fsub_64_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3209433466390790851, 7639918390537419941]
    tran0.writeAction("movir X16 11402")
    tran0.writeAction("slorii X16 X16 12 811")
    tran0.writeAction("slorii X16 X16 12 3006")
    tran0.writeAction("slorii X16 X16 12 1940")
    tran0.writeAction("slorii X16 X16 12 707")
    tran0.writeAction("movir X17 27142")
    tran0.writeAction("slorii X17 X17 12 1812")
    tran0.writeAction("slorii X17 X17 12 3156")
    tran0.writeAction("slorii X17 X17 12 3919")
    tran0.writeAction("slorii X17 X17 12 3237")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
