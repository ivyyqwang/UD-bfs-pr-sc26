from EFA_v2 import *
def addi_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7377915025478373805, -25931]
    tran0.writeAction("movir X16 26211")
    tran0.writeAction("slorii X16 X16 12 2538")
    tran0.writeAction("slorii X16 X16 12 52")
    tran0.writeAction("slorii X16 X16 12 2685")
    tran0.writeAction("slorii X16 X16 12 429")
    tran0.writeAction("addi X16 X17 -25931")
    tran0.writeAction("yieldt")
    return efa
