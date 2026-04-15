from EFA_v2 import *
def add_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2326785428791230868, -5014733216145246604]
    tran0.writeAction("movir X16 8266")
    tran0.writeAction("slorii X16 X16 12 1648")
    tran0.writeAction("slorii X16 X16 12 1287")
    tran0.writeAction("slorii X16 X16 12 2688")
    tran0.writeAction("slorii X16 X16 12 404")
    tran0.writeAction("movir X17 47720")
    tran0.writeAction("slorii X17 X17 12 363")
    tran0.writeAction("slorii X17 X17 12 1416")
    tran0.writeAction("slorii X17 X17 12 1271")
    tran0.writeAction("slorii X17 X17 12 1652")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
