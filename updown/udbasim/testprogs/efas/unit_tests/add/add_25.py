from EFA_v2 import *
def add_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7360195326868059903, 7537105516268853014]
    tran0.writeAction("movir X16 26148")
    tran0.writeAction("slorii X16 X16 12 2730")
    tran0.writeAction("slorii X16 X16 12 1887")
    tran0.writeAction("slorii X16 X16 12 1887")
    tran0.writeAction("slorii X16 X16 12 1791")
    tran0.writeAction("movir X17 26777")
    tran0.writeAction("slorii X17 X17 12 728")
    tran0.writeAction("slorii X17 X17 12 2211")
    tran0.writeAction("slorii X17 X17 12 3449")
    tran0.writeAction("slorii X17 X17 12 1814")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
