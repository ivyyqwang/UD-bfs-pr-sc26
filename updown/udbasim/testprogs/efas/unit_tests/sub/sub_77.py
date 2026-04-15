from EFA_v2 import *
def sub_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3069810740457595916, 8284457346605114385]
    tran0.writeAction("movir X16 10906")
    tran0.writeAction("slorii X16 X16 12 649")
    tran0.writeAction("slorii X16 X16 12 2712")
    tran0.writeAction("slorii X16 X16 12 2678")
    tran0.writeAction("slorii X16 X16 12 1036")
    tran0.writeAction("movir X17 29432")
    tran0.writeAction("slorii X17 X17 12 1249")
    tran0.writeAction("slorii X17 X17 12 85")
    tran0.writeAction("slorii X17 X17 12 1118")
    tran0.writeAction("slorii X17 X17 12 1041")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
