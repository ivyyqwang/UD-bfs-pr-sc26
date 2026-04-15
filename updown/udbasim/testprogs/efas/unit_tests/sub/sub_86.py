from EFA_v2 import *
def sub_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8739260248259717661, -9025908584434912596]
    tran0.writeAction("movir X16 34487")
    tran0.writeAction("slorii X16 X16 12 3729")
    tran0.writeAction("slorii X16 X16 12 2902")
    tran0.writeAction("slorii X16 X16 12 3225")
    tran0.writeAction("slorii X16 X16 12 1507")
    tran0.writeAction("movir X17 33469")
    tran0.writeAction("slorii X17 X17 12 2175")
    tran0.writeAction("slorii X17 X17 12 1721")
    tran0.writeAction("slorii X17 X17 12 2491")
    tran0.writeAction("slorii X17 X17 12 684")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
