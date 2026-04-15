from EFA_v2 import *
def sub_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8382271264836648184, 4374558411027852043]
    tran0.writeAction("movir X16 35756")
    tran0.writeAction("slorii X16 X16 12 779")
    tran0.writeAction("slorii X16 X16 12 544")
    tran0.writeAction("slorii X16 X16 12 1832")
    tran0.writeAction("slorii X16 X16 12 776")
    tran0.writeAction("movir X17 15541")
    tran0.writeAction("slorii X17 X17 12 2267")
    tran0.writeAction("slorii X17 X17 12 650")
    tran0.writeAction("slorii X17 X17 12 2098")
    tran0.writeAction("slorii X17 X17 12 2827")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
