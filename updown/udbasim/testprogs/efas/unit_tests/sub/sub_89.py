from EFA_v2 import *
def sub_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5287559809594871637, 6744121294239013095]
    tran0.writeAction("movir X16 18785")
    tran0.writeAction("slorii X16 X16 12 762")
    tran0.writeAction("slorii X16 X16 12 467")
    tran0.writeAction("slorii X16 X16 12 2188")
    tran0.writeAction("slorii X16 X16 12 3925")
    tran0.writeAction("movir X17 23959")
    tran0.writeAction("slorii X17 X17 12 3817")
    tran0.writeAction("slorii X17 X17 12 1489")
    tran0.writeAction("slorii X17 X17 12 1081")
    tran0.writeAction("slorii X17 X17 12 2279")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
