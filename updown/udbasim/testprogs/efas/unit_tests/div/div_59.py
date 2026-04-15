from EFA_v2 import *
def div_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1748518714626335552, 9055644690578045298]
    tran0.writeAction("movir X16 6211")
    tran0.writeAction("slorii X16 X16 12 4040")
    tran0.writeAction("slorii X16 X16 12 452")
    tran0.writeAction("slorii X16 X16 12 1742")
    tran0.writeAction("slorii X16 X16 12 832")
    tran0.writeAction("movir X17 32172")
    tran0.writeAction("slorii X17 X17 12 461")
    tran0.writeAction("slorii X17 X17 12 3586")
    tran0.writeAction("slorii X17 X17 12 231")
    tran0.writeAction("slorii X17 X17 12 2418")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
