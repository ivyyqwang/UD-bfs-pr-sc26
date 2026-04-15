from EFA_v2 import *
def srsubii_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6351051508909507898, 10, 691]
    tran0.writeAction("movir X16 42972")
    tran0.writeAction("slorii X16 X16 12 2180")
    tran0.writeAction("slorii X16 X16 12 3405")
    tran0.writeAction("slorii X16 X16 12 983")
    tran0.writeAction("slorii X16 X16 12 2758")
    tran0.writeAction("srsubii X16 X17 10 691")
    tran0.writeAction("yieldt")
    return efa
