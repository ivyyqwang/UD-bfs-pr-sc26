from EFA_v2 import *
def fmul_64_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13614616095385532279, 4046232882247495939]
    tran0.writeAction("movir X16 48368")
    tran0.writeAction("slorii X16 X16 12 3411")
    tran0.writeAction("slorii X16 X16 12 1174")
    tran0.writeAction("slorii X16 X16 12 3155")
    tran0.writeAction("slorii X16 X16 12 1911")
    tran0.writeAction("movir X17 14375")
    tran0.writeAction("slorii X17 X17 12 437")
    tran0.writeAction("slorii X17 X17 12 3672")
    tran0.writeAction("slorii X17 X17 12 3551")
    tran0.writeAction("slorii X17 X17 12 259")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
