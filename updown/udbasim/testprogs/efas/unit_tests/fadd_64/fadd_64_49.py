from EFA_v2 import *
def fadd_64_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13385928274580746454, 14334143226327059580]
    tran0.writeAction("movir X16 47556")
    tran0.writeAction("slorii X16 X16 12 1517")
    tran0.writeAction("slorii X16 X16 12 2067")
    tran0.writeAction("slorii X16 X16 12 995")
    tran0.writeAction("slorii X16 X16 12 214")
    tran0.writeAction("movir X17 50925")
    tran0.writeAction("slorii X17 X17 12 437")
    tran0.writeAction("slorii X17 X17 12 412")
    tran0.writeAction("slorii X17 X17 12 3260")
    tran0.writeAction("slorii X17 X17 12 3196")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
