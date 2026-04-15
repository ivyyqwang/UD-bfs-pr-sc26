from EFA_v2 import *
def addi_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2502051345529894694, 19048]
    tran0.writeAction("movir X16 8889")
    tran0.writeAction("slorii X16 X16 12 295")
    tran0.writeAction("slorii X16 X16 12 316")
    tran0.writeAction("slorii X16 X16 12 399")
    tran0.writeAction("slorii X16 X16 12 1830")
    tran0.writeAction("addi X16 X17 19048")
    tran0.writeAction("yieldt")
    return efa
