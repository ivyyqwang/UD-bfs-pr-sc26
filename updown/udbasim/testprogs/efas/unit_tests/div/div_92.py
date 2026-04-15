from EFA_v2 import *
def div_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1012290169707096970, 69314431921855445]
    tran0.writeAction("movir X16 3596")
    tran0.writeAction("slorii X16 X16 12 1544")
    tran0.writeAction("slorii X16 X16 12 3015")
    tran0.writeAction("slorii X16 X16 12 46")
    tran0.writeAction("slorii X16 X16 12 2954")
    tran0.writeAction("movir X17 246")
    tran0.writeAction("slorii X17 X17 12 1041")
    tran0.writeAction("slorii X17 X17 12 3020")
    tran0.writeAction("slorii X17 X17 12 2089")
    tran0.writeAction("slorii X17 X17 12 3029")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
