from EFA_v2 import *
def fadd_64_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14105770534410285025, 8680914374468348508]
    tran0.writeAction("movir X16 50113")
    tran0.writeAction("slorii X16 X16 12 3129")
    tran0.writeAction("slorii X16 X16 12 194")
    tran0.writeAction("slorii X16 X16 12 2854")
    tran0.writeAction("slorii X16 X16 12 4065")
    tran0.writeAction("movir X17 30840")
    tran0.writeAction("slorii X17 X17 12 3290")
    tran0.writeAction("slorii X17 X17 12 335")
    tran0.writeAction("slorii X17 X17 12 3146")
    tran0.writeAction("slorii X17 X17 12 2652")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
