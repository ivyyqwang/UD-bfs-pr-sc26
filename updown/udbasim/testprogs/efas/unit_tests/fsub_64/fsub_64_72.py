from EFA_v2 import *
def fsub_64_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2201857210548326817, 873812779767668850]
    tran0.writeAction("movir X16 7822")
    tran0.writeAction("slorii X16 X16 12 2327")
    tran0.writeAction("slorii X16 X16 12 1936")
    tran0.writeAction("slorii X16 X16 12 3545")
    tran0.writeAction("slorii X16 X16 12 417")
    tran0.writeAction("movir X17 3104")
    tran0.writeAction("slorii X17 X17 12 1665")
    tran0.writeAction("slorii X17 X17 12 2034")
    tran0.writeAction("slorii X17 X17 12 1018")
    tran0.writeAction("slorii X17 X17 12 114")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
