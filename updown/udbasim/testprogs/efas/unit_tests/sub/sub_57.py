from EFA_v2 import *
def sub_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7282163603138938840, -8543076589912160861]
    tran0.writeAction("movir X16 25871")
    tran0.writeAction("slorii X16 X16 12 1811")
    tran0.writeAction("slorii X16 X16 12 1769")
    tran0.writeAction("slorii X16 X16 12 1536")
    tran0.writeAction("slorii X16 X16 12 2008")
    tran0.writeAction("movir X17 35184")
    tran0.writeAction("slorii X17 X17 12 3665")
    tran0.writeAction("slorii X17 X17 12 2761")
    tran0.writeAction("slorii X17 X17 12 1352")
    tran0.writeAction("slorii X17 X17 12 1443")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
