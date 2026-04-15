from EFA_v2 import *
def fmadd_64_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1524633107041534258, 10026925834974214962, 16223435075636202001]
    tran0.writeAction("movir X16 5416")
    tran0.writeAction("slorii X16 X16 12 2395")
    tran0.writeAction("slorii X16 X16 12 2982")
    tran0.writeAction("slorii X16 X16 12 44")
    tran0.writeAction("slorii X16 X16 12 306")
    tran0.writeAction("movir X17 35622")
    tran0.writeAction("slorii X17 X17 12 3262")
    tran0.writeAction("slorii X17 X17 12 3078")
    tran0.writeAction("slorii X17 X17 12 3379")
    tran0.writeAction("slorii X17 X17 12 2866")
    tran0.writeAction("movir X18 57637")
    tran0.writeAction("slorii X18 X18 12 899")
    tran0.writeAction("slorii X18 X18 12 3823")
    tran0.writeAction("slorii X18 X18 12 3720")
    tran0.writeAction("slorii X18 X18 12 2577")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
