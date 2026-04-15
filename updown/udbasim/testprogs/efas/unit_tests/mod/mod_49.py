from EFA_v2 import *
def mod_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [131607970817801469, 546630622671368325]
    tran0.writeAction("movir X16 467")
    tran0.writeAction("slorii X16 X16 12 2316")
    tran0.writeAction("slorii X16 X16 12 142")
    tran0.writeAction("slorii X16 X16 12 839")
    tran0.writeAction("slorii X16 X16 12 3325")
    tran0.writeAction("movir X17 1942")
    tran0.writeAction("slorii X17 X17 12 90")
    tran0.writeAction("slorii X17 X17 12 1975")
    tran0.writeAction("slorii X17 X17 12 2775")
    tran0.writeAction("slorii X17 X17 12 133")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
