from EFA_v2 import *
def addi_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4506700450775855712, -19303]
    tran0.writeAction("movir X16 49524")
    tran0.writeAction("slorii X16 X16 12 4029")
    tran0.writeAction("slorii X16 X16 12 330")
    tran0.writeAction("slorii X16 X16 12 1688")
    tran0.writeAction("slorii X16 X16 12 3488")
    tran0.writeAction("addi X16 X17 -19303")
    tran0.writeAction("yieldt")
    return efa
