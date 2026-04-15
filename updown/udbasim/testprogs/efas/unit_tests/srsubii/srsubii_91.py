from EFA_v2 import *
def srsubii_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7103426923745737713, 14, 1200]
    tran0.writeAction("movir X16 40299")
    tran0.writeAction("slorii X16 X16 12 2285")
    tran0.writeAction("slorii X16 X16 12 2354")
    tran0.writeAction("slorii X16 X16 12 776")
    tran0.writeAction("slorii X16 X16 12 1039")
    tran0.writeAction("srsubii X16 X17 14 1200")
    tran0.writeAction("yieldt")
    return efa
