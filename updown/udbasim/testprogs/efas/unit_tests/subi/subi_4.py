from EFA_v2 import *
def subi_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4318991566380129591, 21522]
    tran0.writeAction("movir X16 50191")
    tran0.writeAction("slorii X16 X16 12 3520")
    tran0.writeAction("slorii X16 X16 12 3498")
    tran0.writeAction("slorii X16 X16 12 18")
    tran0.writeAction("slorii X16 X16 12 713")
    tran0.writeAction("subi X16 X17 21522")
    tran0.writeAction("yieldt")
    return efa
