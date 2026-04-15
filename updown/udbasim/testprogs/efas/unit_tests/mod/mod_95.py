from EFA_v2 import *
def mod_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5525566935609733313, -5587724769368245810]
    tran0.writeAction("movir X16 45905")
    tran0.writeAction("slorii X16 X16 12 994")
    tran0.writeAction("slorii X16 X16 12 1492")
    tran0.writeAction("slorii X16 X16 12 1384")
    tran0.writeAction("slorii X16 X16 12 3903")
    tran0.writeAction("movir X17 45684")
    tran0.writeAction("slorii X17 X17 12 1694")
    tran0.writeAction("slorii X17 X17 12 3427")
    tran0.writeAction("slorii X17 X17 12 631")
    tran0.writeAction("slorii X17 X17 12 2510")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
