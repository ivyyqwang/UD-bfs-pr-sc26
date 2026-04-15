from EFA_v2 import *
def mod_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7303968612319969229, -1505174535867739576]
    tran0.writeAction("movir X16 39587")
    tran0.writeAction("slorii X16 X16 12 371")
    tran0.writeAction("slorii X16 X16 12 3780")
    tran0.writeAction("slorii X16 X16 12 268")
    tran0.writeAction("slorii X16 X16 12 51")
    tran0.writeAction("movir X17 60188")
    tran0.writeAction("slorii X17 X17 12 2235")
    tran0.writeAction("slorii X17 X17 12 3072")
    tran0.writeAction("slorii X17 X17 12 2621")
    tran0.writeAction("slorii X17 X17 12 584")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
