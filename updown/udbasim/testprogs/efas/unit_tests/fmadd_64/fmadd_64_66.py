from EFA_v2 import *
def fmadd_64_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14531840904145645417, 6466654529151935157, 12465436629679949841]
    tran0.writeAction("movir X16 51627")
    tran0.writeAction("slorii X16 X16 12 1924")
    tran0.writeAction("slorii X16 X16 12 3888")
    tran0.writeAction("slorii X16 X16 12 378")
    tran0.writeAction("slorii X16 X16 12 3945")
    tran0.writeAction("movir X17 22974")
    tran0.writeAction("slorii X17 X17 12 704")
    tran0.writeAction("slorii X17 X17 12 2127")
    tran0.writeAction("slorii X17 X17 12 1114")
    tran0.writeAction("slorii X17 X17 12 693")
    tran0.writeAction("movir X18 44286")
    tran0.writeAction("slorii X18 X18 12 521")
    tran0.writeAction("slorii X18 X18 12 490")
    tran0.writeAction("slorii X18 X18 12 884")
    tran0.writeAction("slorii X18 X18 12 2065")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
