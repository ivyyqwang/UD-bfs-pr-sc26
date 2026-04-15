from EFA_v2 import *
def mod_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4320108761134581968, 8316302024786462128]
    tran0.writeAction("movir X16 15348")
    tran0.writeAction("slorii X16 X16 12 448")
    tran0.writeAction("slorii X16 X16 12 1922")
    tran0.writeAction("slorii X16 X16 12 1964")
    tran0.writeAction("slorii X16 X16 12 2256")
    tran0.writeAction("movir X17 29545")
    tran0.writeAction("slorii X17 X17 12 1802")
    tran0.writeAction("slorii X17 X17 12 320")
    tran0.writeAction("slorii X17 X17 12 1060")
    tran0.writeAction("slorii X17 X17 12 1456")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
