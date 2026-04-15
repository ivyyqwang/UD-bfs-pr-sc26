from EFA_v2 import *
def div_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7901978376365954546, -2807255852800963774]
    tran0.writeAction("movir X16 28073")
    tran0.writeAction("slorii X16 X16 12 1911")
    tran0.writeAction("slorii X16 X16 12 1922")
    tran0.writeAction("slorii X16 X16 12 453")
    tran0.writeAction("slorii X16 X16 12 1522")
    tran0.writeAction("movir X17 55562")
    tran0.writeAction("slorii X17 X17 12 2554")
    tran0.writeAction("slorii X17 X17 12 3300")
    tran0.writeAction("slorii X17 X17 12 664")
    tran0.writeAction("slorii X17 X17 12 2882")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
