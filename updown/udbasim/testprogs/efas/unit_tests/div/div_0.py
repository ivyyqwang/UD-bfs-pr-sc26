from EFA_v2 import *
def div_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2712485322676059967, 2121593647151415300]
    tran0.writeAction("movir X16 55899")
    tran0.writeAction("slorii X16 X16 12 1295")
    tran0.writeAction("slorii X16 X16 12 2155")
    tran0.writeAction("slorii X16 X16 12 1772")
    tran0.writeAction("slorii X16 X16 12 193")
    tran0.writeAction("movir X17 7537")
    tran0.writeAction("slorii X17 X17 12 1698")
    tran0.writeAction("slorii X17 X17 12 3696")
    tran0.writeAction("slorii X17 X17 12 760")
    tran0.writeAction("slorii X17 X17 12 4")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
