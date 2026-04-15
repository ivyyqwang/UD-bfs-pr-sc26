from EFA_v2 import *
def mul_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7525564108600647079, -7571083486774053237]
    tran0.writeAction("movir X16 26736")
    tran0.writeAction("slorii X16 X16 12 714")
    tran0.writeAction("slorii X16 X16 12 3907")
    tran0.writeAction("slorii X16 X16 12 2337")
    tran0.writeAction("slorii X16 X16 12 3495")
    tran0.writeAction("movir X17 38638")
    tran0.writeAction("slorii X17 X17 12 442")
    tran0.writeAction("slorii X17 X17 12 3742")
    tran0.writeAction("slorii X17 X17 12 27")
    tran0.writeAction("slorii X17 X17 12 1675")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
