from EFA_v2 import *
def subi_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3441174114504078822, 11169]
    tran0.writeAction("movir X16 53310")
    tran0.writeAction("slorii X16 X16 12 2021")
    tran0.writeAction("slorii X16 X16 12 4094")
    tran0.writeAction("slorii X16 X16 12 2928")
    tran0.writeAction("slorii X16 X16 12 2586")
    tran0.writeAction("subi X16 X17 11169")
    tran0.writeAction("yieldt")
    return efa
