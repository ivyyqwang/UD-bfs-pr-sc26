from EFA_v2 import *
def fsub_64_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13952608173104421465, 10873249463184938183]
    tran0.writeAction("movir X16 49569")
    tran0.writeAction("slorii X16 X16 12 2547")
    tran0.writeAction("slorii X16 X16 12 1432")
    tran0.writeAction("slorii X16 X16 12 413")
    tran0.writeAction("slorii X16 X16 12 2649")
    tran0.writeAction("movir X17 38629")
    tran0.writeAction("slorii X17 X17 12 2220")
    tran0.writeAction("slorii X17 X17 12 1823")
    tran0.writeAction("slorii X17 X17 12 1413")
    tran0.writeAction("slorii X17 X17 12 1223")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
