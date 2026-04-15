from EFA_v2 import *
def fdiv_64_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1782189776482803439, 5985273637263741000]
    tran0.writeAction("movir X16 6331")
    tran0.writeAction("slorii X16 X16 12 2498")
    tran0.writeAction("slorii X16 X16 12 2245")
    tran0.writeAction("slorii X16 X16 12 2417")
    tran0.writeAction("slorii X16 X16 12 3823")
    tran0.writeAction("movir X17 21263")
    tran0.writeAction("slorii X17 X17 12 3946")
    tran0.writeAction("slorii X17 X17 12 2408")
    tran0.writeAction("slorii X17 X17 12 2521")
    tran0.writeAction("slorii X17 X17 12 72")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
