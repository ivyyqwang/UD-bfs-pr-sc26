from EFA_v2 import *
def addi_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2555061047162610825, -23062]
    tran0.writeAction("movir X16 9077")
    tran0.writeAction("slorii X16 X16 12 1639")
    tran0.writeAction("slorii X16 X16 12 3119")
    tran0.writeAction("slorii X16 X16 12 2314")
    tran0.writeAction("slorii X16 X16 12 1161")
    tran0.writeAction("addi X16 X17 -23062")
    tran0.writeAction("yieldt")
    return efa
