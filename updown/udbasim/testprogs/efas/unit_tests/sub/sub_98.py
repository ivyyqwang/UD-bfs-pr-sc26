from EFA_v2 import *
def sub_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3071343337329347388, -1659429257298853990]
    tran0.writeAction("movir X16 54624")
    tran0.writeAction("slorii X16 X16 12 1624")
    tran0.writeAction("slorii X16 X16 12 483")
    tran0.writeAction("slorii X16 X16 12 907")
    tran0.writeAction("slorii X16 X16 12 1220")
    tran0.writeAction("movir X17 59640")
    tran0.writeAction("slorii X17 X17 12 2142")
    tran0.writeAction("slorii X17 X17 12 492")
    tran0.writeAction("slorii X17 X17 12 3323")
    tran0.writeAction("slorii X17 X17 12 3994")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
