from EFA_v2 import *
def fmul_64_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15218537586333295319, 13747080181132921349]
    tran0.writeAction("movir X16 54067")
    tran0.writeAction("slorii X16 X16 12 436")
    tran0.writeAction("slorii X16 X16 12 3506")
    tran0.writeAction("slorii X16 X16 12 1338")
    tran0.writeAction("slorii X16 X16 12 727")
    tran0.writeAction("movir X17 48839")
    tran0.writeAction("slorii X17 X17 12 1801")
    tran0.writeAction("slorii X17 X17 12 1775")
    tran0.writeAction("slorii X17 X17 12 984")
    tran0.writeAction("slorii X17 X17 12 2565")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
