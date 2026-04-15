from EFA_v2 import *
def srsubii_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6097553020878418275, 15, 1509]
    tran0.writeAction("movir X16 43873")
    tran0.writeAction("slorii X16 X16 12 573")
    tran0.writeAction("slorii X16 X16 12 1391")
    tran0.writeAction("slorii X16 X16 12 1768")
    tran0.writeAction("slorii X16 X16 12 3741")
    tran0.writeAction("srsubii X16 X17 15 1509")
    tran0.writeAction("yieldt")
    return efa
