from EFA_v2 import *
def slsubii_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8792711963167974410, 0, 454]
    tran0.writeAction("movir X16 31237")
    tran0.writeAction("slorii X16 X16 12 4047")
    tran0.writeAction("slorii X16 X16 12 472")
    tran0.writeAction("slorii X16 X16 12 3910")
    tran0.writeAction("slorii X16 X16 12 1034")
    tran0.writeAction("slsubii X16 X17 0 454")
    tran0.writeAction("yieldt")
    return efa
