from EFA_v2 import *
def fadd_64_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6368969346647383238, 8808179928156448004]
    tran0.writeAction("movir X16 22627")
    tran0.writeAction("slorii X16 X16 12 510")
    tran0.writeAction("slorii X16 X16 12 100")
    tran0.writeAction("slorii X16 X16 12 1101")
    tran0.writeAction("slorii X16 X16 12 3270")
    tran0.writeAction("movir X17 31292")
    tran0.writeAction("slorii X17 X17 12 3855")
    tran0.writeAction("slorii X17 X17 12 2583")
    tran0.writeAction("slorii X17 X17 12 2010")
    tran0.writeAction("slorii X17 X17 12 1284")
    tran0.writeAction("fadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
