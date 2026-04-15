from EFA_v2 import *
def subi_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8518364177724930181, -20390]
    tran0.writeAction("movir X16 30263")
    tran0.writeAction("slorii X16 X16 12 1265")
    tran0.writeAction("slorii X16 X16 12 1632")
    tran0.writeAction("slorii X16 X16 12 2895")
    tran0.writeAction("slorii X16 X16 12 2181")
    tran0.writeAction("subi X16 X17 -20390")
    tran0.writeAction("yieldt")
    return efa
