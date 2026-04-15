from EFA_v2 import *
def add_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1473754538597538950, 4727153701758380624]
    tran0.writeAction("movir X16 60300")
    tran0.writeAction("slorii X16 X16 12 704")
    tran0.writeAction("slorii X16 X16 12 3632")
    tran0.writeAction("slorii X16 X16 12 3170")
    tran0.writeAction("slorii X16 X16 12 890")
    tran0.writeAction("movir X17 16794")
    tran0.writeAction("slorii X17 X17 12 915")
    tran0.writeAction("slorii X17 X17 12 3847")
    tran0.writeAction("slorii X17 X17 12 4018")
    tran0.writeAction("slorii X17 X17 12 2640")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
