from EFA_v2 import *
def slsubii_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-651579987784773829, 9, 618]
    tran0.writeAction("movir X16 63221")
    tran0.writeAction("slorii X16 X16 12 503")
    tran0.writeAction("slorii X16 X16 12 1037")
    tran0.writeAction("slorii X16 X16 12 1372")
    tran0.writeAction("slorii X16 X16 12 3899")
    tran0.writeAction("slsubii X16 X17 9 618")
    tran0.writeAction("yieldt")
    return efa
