from EFA_v2 import *
def sraddii_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7556029734658454588, 6, 830]
    tran0.writeAction("movir X16 38691")
    tran0.writeAction("slorii X16 X16 12 2415")
    tran0.writeAction("slorii X16 X16 12 3433")
    tran0.writeAction("slorii X16 X16 12 1612")
    tran0.writeAction("slorii X16 X16 12 3012")
    tran0.writeAction("sraddii X16 X17 6 830")
    tran0.writeAction("yieldt")
    return efa
