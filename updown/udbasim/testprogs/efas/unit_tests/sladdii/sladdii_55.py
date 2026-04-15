from EFA_v2 import *
def sladdii_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4927918752430208412, 6, 1343]
    tran0.writeAction("movir X16 17507")
    tran0.writeAction("slorii X16 X16 12 1983")
    tran0.writeAction("slorii X16 X16 12 3840")
    tran0.writeAction("slorii X16 X16 12 2411")
    tran0.writeAction("slorii X16 X16 12 1436")
    tran0.writeAction("sladdii X16 X17 6 1343")
    tran0.writeAction("yieldt")
    return efa
