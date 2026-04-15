from EFA_v2 import *
def mod_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6733331983330047633, 7957746562192461830]
    tran0.writeAction("movir X16 41614")
    tran0.writeAction("slorii X16 X16 12 1635")
    tran0.writeAction("slorii X16 X16 12 3170")
    tran0.writeAction("slorii X16 X16 12 3424")
    tran0.writeAction("slorii X16 X16 12 2415")
    tran0.writeAction("movir X17 28271")
    tran0.writeAction("slorii X17 X17 12 2437")
    tran0.writeAction("slorii X17 X17 12 1564")
    tran0.writeAction("slorii X17 X17 12 277")
    tran0.writeAction("slorii X17 X17 12 6")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
