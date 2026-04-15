from EFA_v2 import *
def srsubii_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5887997494424216541, 11, 816]
    tran0.writeAction("movir X16 44617")
    tran0.writeAction("slorii X16 X16 12 2583")
    tran0.writeAction("slorii X16 X16 12 2442")
    tran0.writeAction("slorii X16 X16 12 1861")
    tran0.writeAction("slorii X16 X16 12 3107")
    tran0.writeAction("srsubii X16 X17 11 816")
    tran0.writeAction("yieldt")
    return efa
