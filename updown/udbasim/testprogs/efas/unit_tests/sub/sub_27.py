from EFA_v2 import *
def sub_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [361269856504914826, -477599047441880889]
    tran0.writeAction("movir X16 1283")
    tran0.writeAction("slorii X16 X16 12 2000")
    tran0.writeAction("slorii X16 X16 12 1337")
    tran0.writeAction("slorii X16 X16 12 130")
    tran0.writeAction("slorii X16 X16 12 906")
    tran0.writeAction("movir X17 63839")
    tran0.writeAction("slorii X17 X17 12 931")
    tran0.writeAction("slorii X17 X17 12 608")
    tran0.writeAction("slorii X17 X17 12 662")
    tran0.writeAction("slorii X17 X17 12 2247")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
