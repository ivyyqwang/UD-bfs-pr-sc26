from EFA_v2 import *
def sub_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3471014001094641684, 6921485850211217099]
    tran0.writeAction("movir X16 12331")
    tran0.writeAction("slorii X16 X16 12 2125")
    tran0.writeAction("slorii X16 X16 12 2049")
    tran0.writeAction("slorii X16 X16 12 2676")
    tran0.writeAction("slorii X16 X16 12 2068")
    tran0.writeAction("movir X17 24590")
    tran0.writeAction("slorii X17 X17 12 235")
    tran0.writeAction("slorii X17 X17 12 1419")
    tran0.writeAction("slorii X17 X17 12 2998")
    tran0.writeAction("slorii X17 X17 12 3787")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
