from EFA_v2 import *
def fsub_64_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2057192989844977540, 17245735870403519039]
    tran0.writeAction("movir X16 7308")
    tran0.writeAction("slorii X16 X16 12 2529")
    tran0.writeAction("slorii X16 X16 12 4082")
    tran0.writeAction("slorii X16 X16 12 547")
    tran0.writeAction("slorii X16 X16 12 1924")
    tran0.writeAction("movir X17 61269")
    tran0.writeAction("slorii X17 X17 12 662")
    tran0.writeAction("slorii X17 X17 12 1789")
    tran0.writeAction("slorii X17 X17 12 2514")
    tran0.writeAction("slorii X17 X17 12 575")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
