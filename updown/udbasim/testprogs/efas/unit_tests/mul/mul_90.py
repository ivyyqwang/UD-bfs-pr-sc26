from EFA_v2 import *
def mul_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7546693808775178515, -3493807634137432876]
    tran0.writeAction("movir X16 38724")
    tran0.writeAction("slorii X16 X16 12 3103")
    tran0.writeAction("slorii X16 X16 12 1803")
    tran0.writeAction("slorii X16 X16 12 1293")
    tran0.writeAction("slorii X16 X16 12 1773")
    tran0.writeAction("movir X17 53123")
    tran0.writeAction("slorii X17 X17 12 2055")
    tran0.writeAction("slorii X17 X17 12 1981")
    tran0.writeAction("slorii X17 X17 12 2827")
    tran0.writeAction("slorii X17 X17 12 3284")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
