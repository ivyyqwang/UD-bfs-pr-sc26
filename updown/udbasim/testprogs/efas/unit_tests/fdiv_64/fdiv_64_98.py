from EFA_v2 import *
def fdiv_64_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12314527673572907328, 5452674919082704955]
    tran0.writeAction("movir X16 43749")
    tran0.writeAction("slorii X16 X16 12 4058")
    tran0.writeAction("slorii X16 X16 12 3208")
    tran0.writeAction("slorii X16 X16 12 125")
    tran0.writeAction("slorii X16 X16 12 2368")
    tran0.writeAction("movir X17 19371")
    tran0.writeAction("slorii X17 X17 12 3247")
    tran0.writeAction("slorii X17 X17 12 779")
    tran0.writeAction("slorii X17 X17 12 2484")
    tran0.writeAction("slorii X17 X17 12 59")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
