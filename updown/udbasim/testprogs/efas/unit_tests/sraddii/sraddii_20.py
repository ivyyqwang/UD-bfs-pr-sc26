from EFA_v2 import *
def sraddii_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3705402661672747122, 6, 1989]
    tran0.writeAction("movir X16 52371")
    tran0.writeAction("slorii X16 X16 12 3134")
    tran0.writeAction("slorii X16 X16 12 2377")
    tran0.writeAction("slorii X16 X16 12 855")
    tran0.writeAction("slorii X16 X16 12 3982")
    tran0.writeAction("sraddii X16 X17 6 1989")
    tran0.writeAction("yieldt")
    return efa
