from EFA_v2 import *
def srsubii_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6221313953470315409, 8, 404]
    tran0.writeAction("movir X16 43433")
    tran0.writeAction("slorii X16 X16 12 1854")
    tran0.writeAction("slorii X16 X16 12 3031")
    tran0.writeAction("slorii X16 X16 12 904")
    tran0.writeAction("slorii X16 X16 12 1135")
    tran0.writeAction("srsubii X16 X17 8 404")
    tran0.writeAction("yieldt")
    return efa
