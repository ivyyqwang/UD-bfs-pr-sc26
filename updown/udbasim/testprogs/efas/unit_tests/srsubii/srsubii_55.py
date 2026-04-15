from EFA_v2 import *
def srsubii_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2057877955015458321, 11, 1456]
    tran0.writeAction("movir X16 58224")
    tran0.writeAction("slorii X16 X16 12 3886")
    tran0.writeAction("slorii X16 X16 12 1836")
    tran0.writeAction("slorii X16 X16 12 804")
    tran0.writeAction("slorii X16 X16 12 495")
    tran0.writeAction("srsubii X16 X17 11 1456")
    tran0.writeAction("yieldt")
    return efa
