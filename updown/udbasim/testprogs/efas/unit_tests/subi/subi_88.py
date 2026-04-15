from EFA_v2 import *
def subi_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8352088436976833769, 14362]
    tran0.writeAction("movir X16 35863")
    tran0.writeAction("slorii X16 X16 12 1725")
    tran0.writeAction("slorii X16 X16 12 349")
    tran0.writeAction("slorii X16 X16 12 1426")
    tran0.writeAction("slorii X16 X16 12 2839")
    tran0.writeAction("subi X16 X17 14362")
    tran0.writeAction("yieldt")
    return efa
