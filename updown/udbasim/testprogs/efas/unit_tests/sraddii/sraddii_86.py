from EFA_v2 import *
def sraddii_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7749020834400535158, 6, 685]
    tran0.writeAction("movir X16 38005")
    tran0.writeAction("slorii X16 X16 12 3881")
    tran0.writeAction("slorii X16 X16 12 2928")
    tran0.writeAction("slorii X16 X16 12 1863")
    tran0.writeAction("slorii X16 X16 12 3466")
    tran0.writeAction("sraddii X16 X17 6 685")
    tran0.writeAction("yieldt")
    return efa
