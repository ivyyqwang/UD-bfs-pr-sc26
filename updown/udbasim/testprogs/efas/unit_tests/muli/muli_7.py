from EFA_v2 import *
def muli_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6024419660553332214, -25490]
    tran0.writeAction("movir X16 44132")
    tran0.writeAction("slorii X16 X16 12 3939")
    tran0.writeAction("slorii X16 X16 12 3274")
    tran0.writeAction("slorii X16 X16 12 3437")
    tran0.writeAction("slorii X16 X16 12 2570")
    tran0.writeAction("muli X16 X17 -25490")
    tran0.writeAction("yieldt")
    return efa
