from EFA_v2 import *
def fsub_64_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3665799402996424988, 8979286087466933734]
    tran0.writeAction("movir X16 13023")
    tran0.writeAction("slorii X16 X16 12 2194")
    tran0.writeAction("slorii X16 X16 12 641")
    tran0.writeAction("slorii X16 X16 12 1806")
    tran0.writeAction("slorii X16 X16 12 284")
    tran0.writeAction("movir X17 31900")
    tran0.writeAction("slorii X17 X17 12 3409")
    tran0.writeAction("slorii X17 X17 12 3916")
    tran0.writeAction("slorii X17 X17 12 301")
    tran0.writeAction("slorii X17 X17 12 3558")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
