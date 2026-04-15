from EFA_v2 import *
def fadd_64_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5002572897699708621, 7527269849661237194]
    tran0.writeAction("movir X16 17772")
    tran0.writeAction("slorii X16 X16 12 2904")
    tran0.writeAction("slorii X16 X16 12 2994")
    tran0.writeAction("slorii X16 X16 12 1587")
    tran0.writeAction("slorii X16 X16 12 3789")
    tran0.writeAction("movir X17 26742")
    tran0.writeAction("slorii X17 X17 12 960")
    tran0.writeAction("slorii X17 X17 12 3085")
    tran0.writeAction("slorii X17 X17 12 2318")
    tran0.writeAction("slorii X17 X17 12 1994")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
