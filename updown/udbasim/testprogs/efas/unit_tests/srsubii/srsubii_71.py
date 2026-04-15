from EFA_v2 import *
def srsubii_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7636843367443933428, 9, 291]
    tran0.writeAction("movir X16 38404")
    tran0.writeAction("slorii X16 X16 12 1974")
    tran0.writeAction("slorii X16 X16 12 2886")
    tran0.writeAction("slorii X16 X16 12 845")
    tran0.writeAction("slorii X16 X16 12 1804")
    tran0.writeAction("srsubii X16 X17 9 291")
    tran0.writeAction("yieldt")
    return efa
