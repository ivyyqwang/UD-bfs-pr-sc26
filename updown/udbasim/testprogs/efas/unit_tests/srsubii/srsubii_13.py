from EFA_v2 import *
def srsubii_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1783822514028005645, 14, 498]
    tran0.writeAction("movir X16 59198")
    tran0.writeAction("slorii X16 X16 12 2413")
    tran0.writeAction("slorii X16 X16 12 4069")
    tran0.writeAction("slorii X16 X16 12 67")
    tran0.writeAction("slorii X16 X16 12 1779")
    tran0.writeAction("srsubii X16 X17 14 498")
    tran0.writeAction("yieldt")
    return efa
