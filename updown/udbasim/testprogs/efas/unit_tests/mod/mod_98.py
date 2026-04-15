from EFA_v2 import *
def mod_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7497066758207629372, 6339331281091429243]
    tran0.writeAction("movir X16 38901")
    tran0.writeAction("slorii X16 X16 12 280")
    tran0.writeAction("slorii X16 X16 12 299")
    tran0.writeAction("slorii X16 X16 12 2641")
    tran0.writeAction("slorii X16 X16 12 1988")
    tran0.writeAction("movir X17 22521")
    tran0.writeAction("slorii X17 X17 12 3395")
    tran0.writeAction("slorii X17 X17 12 1666")
    tran0.writeAction("slorii X17 X17 12 4000")
    tran0.writeAction("slorii X17 X17 12 891")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
