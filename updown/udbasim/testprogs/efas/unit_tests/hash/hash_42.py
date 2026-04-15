from EFA_v2 import *
def hash_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3222037526329229632, -4740207065993113934]
    tran0.writeAction("movir X16 11446")
    tran0.writeAction("slorii X16 X16 12 4000")
    tran0.writeAction("slorii X16 X16 12 3873")
    tran0.writeAction("slorii X16 X16 12 3408")
    tran0.writeAction("slorii X16 X16 12 320")
    tran0.writeAction("movir X17 48695")
    tran0.writeAction("slorii X17 X17 12 1644")
    tran0.writeAction("slorii X17 X17 12 2501")
    tran0.writeAction("slorii X17 X17 12 2800")
    tran0.writeAction("slorii X17 X17 12 3762")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
