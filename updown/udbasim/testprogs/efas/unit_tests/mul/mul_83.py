from EFA_v2 import *
def mul_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [682995997821042483, -6510491588193004602]
    tran0.writeAction("movir X16 2426")
    tran0.writeAction("slorii X16 X16 12 2003")
    tran0.writeAction("slorii X16 X16 12 3529")
    tran0.writeAction("slorii X16 X16 12 559")
    tran0.writeAction("slorii X16 X16 12 3891")
    tran0.writeAction("movir X17 42406")
    tran0.writeAction("slorii X17 X17 12 358")
    tran0.writeAction("slorii X17 X17 12 1284")
    tran0.writeAction("slorii X17 X17 12 2405")
    tran0.writeAction("slorii X17 X17 12 966")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
