from EFA_v2 import *
def srsubii_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3415549931590501610, 11, 407]
    tran0.writeAction("movir X16 12134")
    tran0.writeAction("slorii X16 X16 12 1929")
    tran0.writeAction("slorii X16 X16 12 257")
    tran0.writeAction("slorii X16 X16 12 252")
    tran0.writeAction("slorii X16 X16 12 1258")
    tran0.writeAction("srsubii X16 X17 11 407")
    tran0.writeAction("yieldt")
    return efa
