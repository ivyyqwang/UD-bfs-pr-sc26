from EFA_v2 import *
def subi_77():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6865280816296446011, 829]
    tran0.writeAction("movir X16 41145")
    tran0.writeAction("slorii X16 X16 12 2551")
    tran0.writeAction("slorii X16 X16 12 2221")
    tran0.writeAction("slorii X16 X16 12 1419")
    tran0.writeAction("slorii X16 X16 12 1989")
    tran0.writeAction("subi X16 X17 829")
    tran0.writeAction("yieldt")
    return efa
