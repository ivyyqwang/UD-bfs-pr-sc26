from EFA_v2 import *
def srsubii_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [852893825013265882, 14, 1827]
    tran0.writeAction("movir X16 3030")
    tran0.writeAction("slorii X16 X16 12 358")
    tran0.writeAction("slorii X16 X16 12 2623")
    tran0.writeAction("slorii X16 X16 12 163")
    tran0.writeAction("slorii X16 X16 12 1498")
    tran0.writeAction("srsubii X16 X17 14 1827")
    tran0.writeAction("yieldt")
    return efa
