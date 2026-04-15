from EFA_v2 import *
def mod_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1670191330317918634, -5191936762766831679]
    tran0.writeAction("movir X16 59602")
    tran0.writeAction("slorii X16 X16 12 1181")
    tran0.writeAction("slorii X16 X16 12 1417")
    tran0.writeAction("slorii X16 X16 12 1897")
    tran0.writeAction("slorii X16 X16 12 3670")
    tran0.writeAction("movir X17 47090")
    tran0.writeAction("slorii X17 X17 12 2192")
    tran0.writeAction("slorii X17 X17 12 1462")
    tran0.writeAction("slorii X17 X17 12 4060")
    tran0.writeAction("slorii X17 X17 12 4033")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
