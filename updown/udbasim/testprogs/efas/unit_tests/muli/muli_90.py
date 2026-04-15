from EFA_v2 import *
def muli_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5225255798790045534, 13593]
    tran0.writeAction("movir X16 18563")
    tran0.writeAction("slorii X16 X16 12 3431")
    tran0.writeAction("slorii X16 X16 12 1763")
    tran0.writeAction("slorii X16 X16 12 1763")
    tran0.writeAction("slorii X16 X16 12 3934")
    tran0.writeAction("muli X16 X17 13593")
    tran0.writeAction("yieldt")
    return efa
