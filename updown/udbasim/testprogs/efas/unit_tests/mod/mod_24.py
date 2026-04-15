from EFA_v2 import *
def mod_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8930781833658489790, 7954906624125477901]
    tran0.writeAction("movir X16 31728")
    tran0.writeAction("slorii X16 X16 12 2092")
    tran0.writeAction("slorii X16 X16 12 681")
    tran0.writeAction("slorii X16 X16 12 2973")
    tran0.writeAction("slorii X16 X16 12 3006")
    tran0.writeAction("movir X17 28261")
    tran0.writeAction("slorii X17 X17 12 2070")
    tran0.writeAction("slorii X17 X17 12 3456")
    tran0.writeAction("slorii X17 X17 12 1642")
    tran0.writeAction("slorii X17 X17 12 1037")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
