from EFA_v2 import *
def sladdii_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5570095401040643859, 13, 1212]
    tran0.writeAction("movir X16 45747")
    tran0.writeAction("slorii X16 X16 12 187")
    tran0.writeAction("slorii X16 X16 12 3727")
    tran0.writeAction("slorii X16 X16 12 3831")
    tran0.writeAction("slorii X16 X16 12 2285")
    tran0.writeAction("sladdii X16 X17 13 1212")
    tran0.writeAction("yieldt")
    return efa
