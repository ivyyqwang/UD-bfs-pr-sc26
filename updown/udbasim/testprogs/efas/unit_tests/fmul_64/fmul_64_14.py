from EFA_v2 import *
def fmul_64_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [86058334963987221, 12367784238242286888]
    tran0.writeAction("movir X16 305")
    tran0.writeAction("slorii X16 X16 12 3033")
    tran0.writeAction("slorii X16 X16 12 2437")
    tran0.writeAction("slorii X16 X16 12 2007")
    tran0.writeAction("slorii X16 X16 12 789")
    tran0.writeAction("movir X17 43939")
    tran0.writeAction("slorii X17 X17 12 803")
    tran0.writeAction("slorii X17 X17 12 3267")
    tran0.writeAction("slorii X17 X17 12 436")
    tran0.writeAction("slorii X17 X17 12 3368")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
