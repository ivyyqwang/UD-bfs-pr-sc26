from EFA_v2 import *
def fsub_64_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13533642797297166084, 5697073204019658675]
    tran0.writeAction("movir X16 48081")
    tran0.writeAction("slorii X16 X16 12 646")
    tran0.writeAction("slorii X16 X16 12 2937")
    tran0.writeAction("slorii X16 X16 12 3774")
    tran0.writeAction("slorii X16 X16 12 1796")
    tran0.writeAction("movir X17 20240")
    tran0.writeAction("slorii X17 X17 12 286")
    tran0.writeAction("slorii X17 X17 12 1288")
    tran0.writeAction("slorii X17 X17 12 4047")
    tran0.writeAction("slorii X17 X17 12 4019")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
