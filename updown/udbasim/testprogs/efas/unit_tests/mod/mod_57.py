from EFA_v2 import *
def mod_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8838613178305467124, 3125271658975203412]
    tran0.writeAction("movir X16 34134")
    tran0.writeAction("slorii X16 X16 12 3842")
    tran0.writeAction("slorii X16 X16 12 1200")
    tran0.writeAction("slorii X16 X16 12 66")
    tran0.writeAction("slorii X16 X16 12 3340")
    tran0.writeAction("movir X17 11103")
    tran0.writeAction("slorii X17 X17 12 800")
    tran0.writeAction("slorii X17 X17 12 1011")
    tran0.writeAction("slorii X17 X17 12 3329")
    tran0.writeAction("slorii X17 X17 12 84")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
