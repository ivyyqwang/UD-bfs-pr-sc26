from EFA_v2 import *
def hash_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1368087600756200360, -231149103302193549]
    tran0.writeAction("movir X16 60675")
    tran0.writeAction("slorii X16 X16 12 2361")
    tran0.writeAction("slorii X16 X16 12 855")
    tran0.writeAction("slorii X16 X16 12 1270")
    tran0.writeAction("slorii X16 X16 12 3160")
    tran0.writeAction("movir X17 64714")
    tran0.writeAction("slorii X17 X17 12 3249")
    tran0.writeAction("slorii X17 X17 12 3455")
    tran0.writeAction("slorii X17 X17 12 2140")
    tran0.writeAction("slorii X17 X17 12 3699")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
