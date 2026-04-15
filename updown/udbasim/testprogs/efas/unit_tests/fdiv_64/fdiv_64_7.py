from EFA_v2 import *
def fdiv_64_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5976839963369900906, 9821030645326346419]
    tran0.writeAction("movir X16 21234")
    tran0.writeAction("slorii X16 X16 12 4")
    tran0.writeAction("slorii X16 X16 12 1968")
    tran0.writeAction("slorii X16 X16 12 88")
    tran0.writeAction("slorii X16 X16 12 2922")
    tran0.writeAction("movir X17 34891")
    tran0.writeAction("slorii X17 X17 12 1269")
    tran0.writeAction("slorii X17 X17 12 1662")
    tran0.writeAction("slorii X17 X17 12 3695")
    tran0.writeAction("slorii X17 X17 12 2227")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
