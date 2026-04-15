from EFA_v2 import *
def subi_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6857284201396339309, 17321]
    tran0.writeAction("movir X16 24361")
    tran0.writeAction("slorii X16 X16 12 3962")
    tran0.writeAction("slorii X16 X16 12 1620")
    tran0.writeAction("slorii X16 X16 12 520")
    tran0.writeAction("slorii X16 X16 12 621")
    tran0.writeAction("subi X16 X17 17321")
    tran0.writeAction("yieldt")
    return efa
