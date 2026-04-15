from EFA_v2 import *
def fsqrt_64_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2573681675759930444]
    tran0.writeAction("movir X16 9143")
    tran0.writeAction("slorii X16 X16 12 2269")
    tran0.writeAction("slorii X16 X16 12 2336")
    tran0.writeAction("slorii X16 X16 12 2468")
    tran0.writeAction("slorii X16 X16 12 3148")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
