from EFA_v2 import *
def fdiv_64_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2297571530295982077, 1169600739560074363]
    tran0.writeAction("movir X16 8162")
    tran0.writeAction("slorii X16 X16 12 2514")
    tran0.writeAction("slorii X16 X16 12 573")
    tran0.writeAction("slorii X16 X16 12 1403")
    tran0.writeAction("slorii X16 X16 12 2045")
    tran0.writeAction("movir X17 4155")
    tran0.writeAction("slorii X17 X17 12 1050")
    tran0.writeAction("slorii X17 X17 12 3330")
    tran0.writeAction("slorii X17 X17 12 2098")
    tran0.writeAction("slorii X17 X17 12 3195")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
