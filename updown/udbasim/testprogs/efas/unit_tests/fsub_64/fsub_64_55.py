from EFA_v2 import *
def fsub_64_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4480802397964249290, 11979060267588599567]
    tran0.writeAction("movir X16 15919")
    tran0.writeAction("slorii X16 X16 12 32")
    tran0.writeAction("slorii X16 X16 12 2663")
    tran0.writeAction("slorii X16 X16 12 1546")
    tran0.writeAction("slorii X16 X16 12 2250")
    tran0.writeAction("movir X17 42558")
    tran0.writeAction("slorii X17 X17 12 701")
    tran0.writeAction("slorii X17 X17 12 2168")
    tran0.writeAction("slorii X17 X17 12 2515")
    tran0.writeAction("slorii X17 X17 12 3855")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
