from EFA_v2 import *
def subi_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4831111232533113612, -24055]
    tran0.writeAction("movir X16 48372")
    tran0.writeAction("slorii X16 X16 12 1822")
    tran0.writeAction("slorii X16 X16 12 3626")
    tran0.writeAction("slorii X16 X16 12 1901")
    tran0.writeAction("slorii X16 X16 12 1268")
    tran0.writeAction("subi X16 X17 -24055")
    tran0.writeAction("yieldt")
    return efa
