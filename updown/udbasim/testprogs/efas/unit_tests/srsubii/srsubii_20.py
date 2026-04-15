from EFA_v2 import *
def srsubii_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7047015145236868881, 6, 1886]
    tran0.writeAction("movir X16 25036")
    tran0.writeAction("slorii X16 X16 12 111")
    tran0.writeAction("slorii X16 X16 12 26")
    tran0.writeAction("slorii X16 X16 12 2626")
    tran0.writeAction("slorii X16 X16 12 3857")
    tran0.writeAction("srsubii X16 X17 6 1886")
    tran0.writeAction("yieldt")
    return efa
