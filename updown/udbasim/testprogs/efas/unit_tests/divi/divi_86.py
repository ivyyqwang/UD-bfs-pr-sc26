from EFA_v2 import *
def divi_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9164445407238400473, -12546]
    tran0.writeAction("movir X16 32558")
    tran0.writeAction("slorii X16 X16 12 2664")
    tran0.writeAction("slorii X16 X16 12 2789")
    tran0.writeAction("slorii X16 X16 12 3706")
    tran0.writeAction("slorii X16 X16 12 2521")
    tran0.writeAction("divi X16 X17 -12546")
    tran0.writeAction("yieldt")
    return efa
