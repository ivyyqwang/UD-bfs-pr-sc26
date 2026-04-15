from EFA_v2 import *
def sraddii_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1139207786746651698, 11, 1969]
    tran0.writeAction("movir X16 61488")
    tran0.writeAction("slorii X16 X16 12 2952")
    tran0.writeAction("slorii X16 X16 12 3521")
    tran0.writeAction("slorii X16 X16 12 2485")
    tran0.writeAction("slorii X16 X16 12 3022")
    tran0.writeAction("sraddii X16 X17 11 1969")
    tran0.writeAction("yieldt")
    return efa
