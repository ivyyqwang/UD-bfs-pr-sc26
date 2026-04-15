from EFA_v2 import *
def slsubii_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1865233793428378922, 3, 527]
    tran0.writeAction("movir X16 6626")
    tran0.writeAction("slorii X16 X16 12 2628")
    tran0.writeAction("slorii X16 X16 12 176")
    tran0.writeAction("slorii X16 X16 12 1445")
    tran0.writeAction("slorii X16 X16 12 1322")
    tran0.writeAction("slsubii X16 X17 3 527")
    tran0.writeAction("yieldt")
    return efa
