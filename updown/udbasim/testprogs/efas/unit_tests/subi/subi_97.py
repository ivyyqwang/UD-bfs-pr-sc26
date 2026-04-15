from EFA_v2 import *
def subi_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6929697255990024857, 20940]
    tran0.writeAction("movir X16 24619")
    tran0.writeAction("slorii X16 X16 12 943")
    tran0.writeAction("slorii X16 X16 12 112")
    tran0.writeAction("slorii X16 X16 12 1165")
    tran0.writeAction("slorii X16 X16 12 2713")
    tran0.writeAction("subi X16 X17 20940")
    tran0.writeAction("yieldt")
    return efa
