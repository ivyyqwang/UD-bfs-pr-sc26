from EFA_v2 import *
def add_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5197945565599208044, 4050042536915814586]
    tran0.writeAction("movir X16 18466")
    tran0.writeAction("slorii X16 X16 12 3327")
    tran0.writeAction("slorii X16 X16 12 951")
    tran0.writeAction("slorii X16 X16 12 1465")
    tran0.writeAction("slorii X16 X16 12 620")
    tran0.writeAction("movir X17 14388")
    tran0.writeAction("slorii X17 X17 12 2627")
    tran0.writeAction("slorii X17 X17 12 2738")
    tran0.writeAction("slorii X17 X17 12 364")
    tran0.writeAction("slorii X17 X17 12 2234")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
