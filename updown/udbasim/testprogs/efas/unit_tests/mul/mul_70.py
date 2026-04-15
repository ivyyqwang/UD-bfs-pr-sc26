from EFA_v2 import *
def mul_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6671666968969595242, 2107911918504955607]
    tran0.writeAction("movir X16 41833")
    tran0.writeAction("slorii X16 X16 12 1955")
    tran0.writeAction("slorii X16 X16 12 3422")
    tran0.writeAction("slorii X16 X16 12 3523")
    tran0.writeAction("slorii X16 X16 12 1686")
    tran0.writeAction("movir X17 7488")
    tran0.writeAction("slorii X17 X17 12 3307")
    tran0.writeAction("slorii X17 X17 12 2240")
    tran0.writeAction("slorii X17 X17 12 1228")
    tran0.writeAction("slorii X17 X17 12 3799")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
