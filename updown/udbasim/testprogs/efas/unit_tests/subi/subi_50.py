from EFA_v2 import *
def subi_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5022990422498560220, -7037]
    tran0.writeAction("movir X16 17845")
    tran0.writeAction("slorii X16 X16 12 1010")
    tran0.writeAction("slorii X16 X16 12 3363")
    tran0.writeAction("slorii X16 X16 12 884")
    tran0.writeAction("slorii X16 X16 12 2268")
    tran0.writeAction("subi X16 X17 -7037")
    tran0.writeAction("yieldt")
    return efa
