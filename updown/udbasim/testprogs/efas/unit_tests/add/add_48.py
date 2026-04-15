from EFA_v2 import *
def add_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1874852442027061480, -3167983801402188165]
    tran0.writeAction("movir X16 6660")
    tran0.writeAction("slorii X16 X16 12 3333")
    tran0.writeAction("slorii X16 X16 12 3285")
    tran0.writeAction("slorii X16 X16 12 1215")
    tran0.writeAction("slorii X16 X16 12 232")
    tran0.writeAction("movir X17 54281")
    tran0.writeAction("slorii X17 X17 12 248")
    tran0.writeAction("slorii X17 X17 12 1135")
    tran0.writeAction("slorii X17 X17 12 945")
    tran0.writeAction("slorii X17 X17 12 3707")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
