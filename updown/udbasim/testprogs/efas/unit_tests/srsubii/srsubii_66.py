from EFA_v2 import *
def srsubii_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8287000297387164047, 13, 1399]
    tran0.writeAction("movir X16 29441")
    tran0.writeAction("slorii X16 X16 12 1389")
    tran0.writeAction("slorii X16 X16 12 3379")
    tran0.writeAction("slorii X16 X16 12 1304")
    tran0.writeAction("slorii X16 X16 12 399")
    tran0.writeAction("srsubii X16 X17 13 1399")
    tran0.writeAction("yieldt")
    return efa
