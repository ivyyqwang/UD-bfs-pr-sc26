from EFA_v2 import *
def mod_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6484619544854774813, -8642132411672968849]
    tran0.writeAction("movir X16 42498")
    tran0.writeAction("slorii X16 X16 12 14")
    tran0.writeAction("slorii X16 X16 12 389")
    tran0.writeAction("slorii X16 X16 12 1539")
    tran0.writeAction("slorii X16 X16 12 3043")
    tran0.writeAction("movir X17 34832")
    tran0.writeAction("slorii X17 X17 12 4005")
    tran0.writeAction("slorii X17 X17 12 3084")
    tran0.writeAction("slorii X17 X17 12 1404")
    tran0.writeAction("slorii X17 X17 12 367")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
