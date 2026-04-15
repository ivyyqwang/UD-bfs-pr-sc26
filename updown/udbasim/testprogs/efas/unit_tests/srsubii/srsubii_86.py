from EFA_v2 import *
def srsubii_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7248727410430494293, 6, 260]
    tran0.writeAction("movir X16 25752")
    tran0.writeAction("slorii X16 X16 12 2674")
    tran0.writeAction("slorii X16 X16 12 3236")
    tran0.writeAction("slorii X16 X16 12 1420")
    tran0.writeAction("slorii X16 X16 12 1621")
    tran0.writeAction("srsubii X16 X17 6 260")
    tran0.writeAction("yieldt")
    return efa
