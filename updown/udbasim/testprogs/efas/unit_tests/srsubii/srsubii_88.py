from EFA_v2 import *
def srsubii_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1818306730175405986, 7, 346]
    tran0.writeAction("movir X16 6459")
    tran0.writeAction("slorii X16 X16 12 3781")
    tran0.writeAction("slorii X16 X16 12 1624")
    tran0.writeAction("slorii X16 X16 12 3305")
    tran0.writeAction("slorii X16 X16 12 4002")
    tran0.writeAction("srsubii X16 X17 7 346")
    tran0.writeAction("yieldt")
    return efa
