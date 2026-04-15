from EFA_v2 import *
def fmul_64_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1730720158969224845, 6682999870920776062]
    tran0.writeAction("movir X16 6148")
    tran0.writeAction("slorii X16 X16 12 3085")
    tran0.writeAction("slorii X16 X16 12 152")
    tran0.writeAction("slorii X16 X16 12 3965")
    tran0.writeAction("slorii X16 X16 12 3725")
    tran0.writeAction("movir X17 23742")
    tran0.writeAction("slorii X17 X17 12 3215")
    tran0.writeAction("slorii X17 X17 12 2428")
    tran0.writeAction("slorii X17 X17 12 877")
    tran0.writeAction("slorii X17 X17 12 2430")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
