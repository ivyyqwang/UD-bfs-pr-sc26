from EFA_v2 import *
def fdiv_64_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10844703533589342948, 8140416006761897780]
    tran0.writeAction("movir X16 38528")
    tran0.writeAction("slorii X16 X16 12 518")
    tran0.writeAction("slorii X16 X16 12 2038")
    tran0.writeAction("slorii X16 X16 12 66")
    tran0.writeAction("slorii X16 X16 12 2788")
    tran0.writeAction("movir X17 28920")
    tran0.writeAction("slorii X17 X17 12 2323")
    tran0.writeAction("slorii X17 X17 12 2678")
    tran0.writeAction("slorii X17 X17 12 3877")
    tran0.writeAction("slorii X17 X17 12 3892")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
