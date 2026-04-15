from EFA_v2 import *
def srsubii_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3670170992354361183, 8, 463]
    tran0.writeAction("movir X16 13039")
    tran0.writeAction("slorii X16 X16 12 273")
    tran0.writeAction("slorii X16 X16 12 632")
    tran0.writeAction("slorii X16 X16 12 919")
    tran0.writeAction("slorii X16 X16 12 3935")
    tran0.writeAction("srsubii X16 X17 8 463")
    tran0.writeAction("yieldt")
    return efa
