from EFA_v2 import *
def subi_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8591229042986117912, 17289]
    tran0.writeAction("movir X16 35013")
    tran0.writeAction("slorii X16 X16 12 3371")
    tran0.writeAction("slorii X16 X16 12 1060")
    tran0.writeAction("slorii X16 X16 12 3249")
    tran0.writeAction("slorii X16 X16 12 1256")
    tran0.writeAction("subi X16 X17 17289")
    tran0.writeAction("yieldt")
    return efa
