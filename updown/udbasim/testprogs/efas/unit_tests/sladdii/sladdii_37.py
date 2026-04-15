from EFA_v2 import *
def sladdii_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3965319780103425368, 1, 840]
    tran0.writeAction("movir X16 51448")
    tran0.writeAction("slorii X16 X16 12 1450")
    tran0.writeAction("slorii X16 X16 12 2894")
    tran0.writeAction("slorii X16 X16 12 431")
    tran0.writeAction("slorii X16 X16 12 680")
    tran0.writeAction("sladdii X16 X17 1 840")
    tran0.writeAction("yieldt")
    return efa
