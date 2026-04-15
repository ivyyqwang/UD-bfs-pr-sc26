from EFA_v2 import *
def fsub_64_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5017247527191087533, 14062885674080684132]
    tran0.writeAction("movir X16 17824")
    tran0.writeAction("slorii X16 X16 12 3456")
    tran0.writeAction("slorii X16 X16 12 2848")
    tran0.writeAction("slorii X16 X16 12 1768")
    tran0.writeAction("slorii X16 X16 12 2477")
    tran0.writeAction("movir X17 49961")
    tran0.writeAction("slorii X17 X17 12 1664")
    tran0.writeAction("slorii X17 X17 12 800")
    tran0.writeAction("slorii X17 X17 12 2084")
    tran0.writeAction("slorii X17 X17 12 2148")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
