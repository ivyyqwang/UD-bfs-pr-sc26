from EFA_v2 import *
def fsub_32_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [163992723, 893837226]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 9")
    tran0.writeAction("slorii X16 X16 12 3173")
    tran0.writeAction("slorii X16 X16 12 1171")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 53")
    tran0.writeAction("slorii X17 X17 12 1133")
    tran0.writeAction("slorii X17 X17 12 4010")
    tran0.writeAction("fsub.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
