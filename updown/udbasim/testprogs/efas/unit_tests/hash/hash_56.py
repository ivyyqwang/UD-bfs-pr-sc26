from EFA_v2 import *
def hash_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5089764075564422406, 2072384537264417676]
    tran0.writeAction("movir X16 18082")
    tran0.writeAction("slorii X16 X16 12 1943")
    tran0.writeAction("slorii X16 X16 12 1474")
    tran0.writeAction("slorii X16 X16 12 2301")
    tran0.writeAction("slorii X16 X16 12 1286")
    tran0.writeAction("movir X17 7362")
    tran0.writeAction("slorii X17 X17 12 2412")
    tran0.writeAction("slorii X17 X17 12 437")
    tran0.writeAction("slorii X17 X17 12 2694")
    tran0.writeAction("slorii X17 X17 12 2956")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
