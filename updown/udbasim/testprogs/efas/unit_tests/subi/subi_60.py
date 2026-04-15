from EFA_v2 import *
def subi_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6214447040758466997, -728]
    tran0.writeAction("movir X16 22078")
    tran0.writeAction("slorii X16 X16 12 618")
    tran0.writeAction("slorii X16 X16 12 2163")
    tran0.writeAction("slorii X16 X16 12 3628")
    tran0.writeAction("slorii X16 X16 12 2485")
    tran0.writeAction("subi X16 X17 -728")
    tran0.writeAction("yieldt")
    return efa
