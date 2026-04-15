from EFA_v2 import *
def muli_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4093456220354543887, -20517]
    tran0.writeAction("movir X16 50993")
    tran0.writeAction("slorii X16 X16 12 500")
    tran0.writeAction("slorii X16 X16 12 370")
    tran0.writeAction("slorii X16 X16 12 631")
    tran0.writeAction("slorii X16 X16 12 3825")
    tran0.writeAction("muli X16 X17 -20517")
    tran0.writeAction("yieldt")
    return efa
