from EFA_v2 import *
def mod_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4704615015395057632, -1209178746448480883]
    tran0.writeAction("movir X16 16714")
    tran0.writeAction("slorii X16 X16 12 614")
    tran0.writeAction("slorii X16 X16 12 3629")
    tran0.writeAction("slorii X16 X16 12 2421")
    tran0.writeAction("slorii X16 X16 12 4064")
    tran0.writeAction("movir X17 61240")
    tran0.writeAction("slorii X17 X17 12 549")
    tran0.writeAction("slorii X17 X17 12 1579")
    tran0.writeAction("slorii X17 X17 12 4039")
    tran0.writeAction("slorii X17 X17 12 1421")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
