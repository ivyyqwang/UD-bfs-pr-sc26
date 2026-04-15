from EFA_v2 import *
def add_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8344839017794467958, -1871543988478994217]
    tran0.writeAction("movir X16 35889")
    tran0.writeAction("slorii X16 X16 12 722")
    tran0.writeAction("slorii X16 X16 12 76")
    tran0.writeAction("slorii X16 X16 12 2216")
    tran0.writeAction("slorii X16 X16 12 1930")
    tran0.writeAction("movir X17 58886")
    tran0.writeAction("slorii X17 X17 12 3850")
    tran0.writeAction("slorii X17 X17 12 2185")
    tran0.writeAction("slorii X17 X17 12 785")
    tran0.writeAction("slorii X17 X17 12 2263")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
