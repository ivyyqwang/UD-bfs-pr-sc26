from EFA_v2 import *
def fmadd_64_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11028052000886465414, 13250812420455474202, 4694199803803044844]
    tran0.writeAction("movir X16 39179")
    tran0.writeAction("slorii X16 X16 12 2093")
    tran0.writeAction("slorii X16 X16 12 3485")
    tran0.writeAction("slorii X16 X16 12 1530")
    tran0.writeAction("slorii X16 X16 12 902")
    tran0.writeAction("movir X17 47076")
    tran0.writeAction("slorii X17 X17 12 1403")
    tran0.writeAction("slorii X17 X17 12 202")
    tran0.writeAction("slorii X17 X17 12 2386")
    tran0.writeAction("slorii X17 X17 12 1050")
    tran0.writeAction("movir X18 16677")
    tran0.writeAction("slorii X18 X18 12 605")
    tran0.writeAction("slorii X18 X18 12 2498")
    tran0.writeAction("slorii X18 X18 12 1592")
    tran0.writeAction("slorii X18 X18 12 3052")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
