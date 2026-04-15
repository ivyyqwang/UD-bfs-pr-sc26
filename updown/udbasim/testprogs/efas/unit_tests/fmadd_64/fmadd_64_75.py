from EFA_v2 import *
def fmadd_64_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13284393295254732408, 6928153076799673819, 14339538149721582072]
    tran0.writeAction("movir X16 47195")
    tran0.writeAction("slorii X16 X16 12 2645")
    tran0.writeAction("slorii X16 X16 12 380")
    tran0.writeAction("slorii X16 X16 12 979")
    tran0.writeAction("slorii X16 X16 12 3704")
    tran0.writeAction("movir X17 24613")
    tran0.writeAction("slorii X17 X17 12 3048")
    tran0.writeAction("slorii X17 X17 12 1076")
    tran0.writeAction("slorii X17 X17 12 713")
    tran0.writeAction("slorii X17 X17 12 1499")
    tran0.writeAction("movir X18 50944")
    tran0.writeAction("slorii X18 X18 12 1119")
    tran0.writeAction("slorii X18 X18 12 2329")
    tran0.writeAction("slorii X18 X18 12 1298")
    tran0.writeAction("slorii X18 X18 12 2552")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
