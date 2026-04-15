from EFA_v2 import *
def subi_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6214763608169970458, 30349]
    tran0.writeAction("movir X16 43456")
    tran0.writeAction("slorii X16 X16 12 2966")
    tran0.writeAction("slorii X16 X16 12 3316")
    tran0.writeAction("slorii X16 X16 12 16")
    tran0.writeAction("slorii X16 X16 12 1254")
    tran0.writeAction("subi X16 X17 30349")
    tran0.writeAction("yieldt")
    return efa
