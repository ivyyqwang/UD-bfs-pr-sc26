from EFA_v2 import *
def mod_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-737570370678550403, 585121735215568782]
    tran0.writeAction("movir X16 62915")
    tran0.writeAction("slorii X16 X16 12 2554")
    tran0.writeAction("slorii X16 X16 12 2010")
    tran0.writeAction("slorii X16 X16 12 3489")
    tran0.writeAction("slorii X16 X16 12 125")
    tran0.writeAction("movir X17 2078")
    tran0.writeAction("slorii X17 X17 12 3153")
    tran0.writeAction("slorii X17 X17 12 3641")
    tran0.writeAction("slorii X17 X17 12 3621")
    tran0.writeAction("slorii X17 X17 12 1934")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
