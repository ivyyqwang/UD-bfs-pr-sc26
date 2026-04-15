from EFA_v2 import *
def slsubii_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1935182173304911541, 14, 1140]
    tran0.writeAction("movir X16 6875")
    tran0.writeAction("slorii X16 X16 12 606")
    tran0.writeAction("slorii X16 X16 12 3839")
    tran0.writeAction("slorii X16 X16 12 2079")
    tran0.writeAction("slorii X16 X16 12 1717")
    tran0.writeAction("slsubii X16 X17 14 1140")
    tran0.writeAction("yieldt")
    return efa
