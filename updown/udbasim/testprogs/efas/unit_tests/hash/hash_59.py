from EFA_v2 import *
def hash_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3332804162277161989, -3455682112051865454]
    tran0.writeAction("movir X16 11840")
    tran0.writeAction("slorii X16 X16 12 2043")
    tran0.writeAction("slorii X16 X16 12 2630")
    tran0.writeAction("slorii X16 X16 12 1939")
    tran0.writeAction("slorii X16 X16 12 3077")
    tran0.writeAction("movir X17 53258")
    tran0.writeAction("slorii X17 X17 12 3894")
    tran0.writeAction("slorii X17 X17 12 3478")
    tran0.writeAction("slorii X17 X17 12 1953")
    tran0.writeAction("slorii X17 X17 12 2194")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
