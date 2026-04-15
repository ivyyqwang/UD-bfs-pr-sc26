from EFA_v2 import *
def fsqrt_64_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10794344155578888063]
    tran0.writeAction("movir X16 38349")
    tran0.writeAction("slorii X16 X16 12 877")
    tran0.writeAction("slorii X16 X16 12 400")
    tran0.writeAction("slorii X16 X16 12 2430")
    tran0.writeAction("slorii X16 X16 12 3967")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
