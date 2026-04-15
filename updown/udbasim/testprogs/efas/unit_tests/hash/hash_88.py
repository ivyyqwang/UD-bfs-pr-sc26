from EFA_v2 import *
def hash_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [37035489179511251, 471290171246560244]
    tran0.writeAction("movir X16 131")
    tran0.writeAction("slorii X16 X16 12 2361")
    tran0.writeAction("slorii X16 X16 12 1224")
    tran0.writeAction("slorii X16 X16 12 2570")
    tran0.writeAction("slorii X16 X16 12 2515")
    tran0.writeAction("movir X17 1674")
    tran0.writeAction("slorii X17 X17 12 1470")
    tran0.writeAction("slorii X17 X17 12 2539")
    tran0.writeAction("slorii X17 X17 12 1164")
    tran0.writeAction("slorii X17 X17 12 1012")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
