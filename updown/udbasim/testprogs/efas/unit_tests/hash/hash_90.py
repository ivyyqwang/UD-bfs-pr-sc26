from EFA_v2 import *
def hash_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6360866887177557165, 2828115881533591359]
    tran0.writeAction("movir X16 22598")
    tran0.writeAction("slorii X16 X16 12 1387")
    tran0.writeAction("slorii X16 X16 12 2953")
    tran0.writeAction("slorii X16 X16 12 3125")
    tran0.writeAction("slorii X16 X16 12 1197")
    tran0.writeAction("movir X17 10047")
    tran0.writeAction("slorii X17 X17 12 1990")
    tran0.writeAction("slorii X17 X17 12 2310")
    tran0.writeAction("slorii X17 X17 12 1844")
    tran0.writeAction("slorii X17 X17 12 3903")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
