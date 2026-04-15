from EFA_v2 import *
def subi_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8894531903731540973, -11075]
    tran0.writeAction("movir X16 33936")
    tran0.writeAction("slorii X16 X16 12 1125")
    tran0.writeAction("slorii X16 X16 12 3034")
    tran0.writeAction("slorii X16 X16 12 2877")
    tran0.writeAction("slorii X16 X16 12 3091")
    tran0.writeAction("subi X16 X17 -11075")
    tran0.writeAction("yieldt")
    return efa
