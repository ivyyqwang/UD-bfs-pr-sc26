from EFA_v2 import *
def srsubii_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-509224917688778955, 6, 1926]
    tran0.writeAction("movir X16 63726")
    tran0.writeAction("slorii X16 X16 12 3562")
    tran0.writeAction("slorii X16 X16 12 678")
    tran0.writeAction("slorii X16 X16 12 1567")
    tran0.writeAction("slorii X16 X16 12 3893")
    tran0.writeAction("srsubii X16 X17 6 1926")
    tran0.writeAction("yieldt")
    return efa
