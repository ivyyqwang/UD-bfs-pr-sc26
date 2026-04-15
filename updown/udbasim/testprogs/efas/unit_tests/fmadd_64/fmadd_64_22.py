from EFA_v2 import *
def fmadd_64_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11210005868371869684, 210350117339221963, 2372320070030129453]
    tran0.writeAction("movir X16 39825")
    tran0.writeAction("slorii X16 X16 12 3855")
    tran0.writeAction("slorii X16 X16 12 434")
    tran0.writeAction("slorii X16 X16 12 1431")
    tran0.writeAction("slorii X16 X16 12 4084")
    tran0.writeAction("movir X17 747")
    tran0.writeAction("slorii X17 X17 12 1285")
    tran0.writeAction("slorii X17 X17 12 310")
    tran0.writeAction("slorii X17 X17 12 1908")
    tran0.writeAction("slorii X17 X17 12 4043")
    tran0.writeAction("movir X18 8428")
    tran0.writeAction("slorii X18 X18 12 712")
    tran0.writeAction("slorii X18 X18 12 2267")
    tran0.writeAction("slorii X18 X18 12 2767")
    tran0.writeAction("slorii X18 X18 12 2349")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
