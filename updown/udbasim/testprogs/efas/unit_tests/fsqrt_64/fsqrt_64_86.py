from EFA_v2 import *
def fsqrt_64_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6045297305332238498]
    tran0.writeAction("movir X16 21477")
    tran0.writeAction("slorii X16 X16 12 861")
    tran0.writeAction("slorii X16 X16 12 3757")
    tran0.writeAction("slorii X16 X16 12 3908")
    tran0.writeAction("slorii X16 X16 12 2210")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
