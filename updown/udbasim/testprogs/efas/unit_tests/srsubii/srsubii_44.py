from EFA_v2 import *
def srsubii_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3084842012385163420, 3, 1924]
    tran0.writeAction("movir X16 54576")
    tran0.writeAction("slorii X16 X16 12 1800")
    tran0.writeAction("slorii X16 X16 12 2223")
    tran0.writeAction("slorii X16 X16 12 2380")
    tran0.writeAction("slorii X16 X16 12 1892")
    tran0.writeAction("srsubii X16 X17 3 1924")
    tran0.writeAction("yieldt")
    return efa
