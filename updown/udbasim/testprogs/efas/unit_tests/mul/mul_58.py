from EFA_v2 import *
def mul_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5151122899596088439, 1111043494882039874]
    tran0.writeAction("movir X16 18300")
    tran0.writeAction("slorii X16 X16 12 1903")
    tran0.writeAction("slorii X16 X16 12 3136")
    tran0.writeAction("slorii X16 X16 12 3297")
    tran0.writeAction("slorii X16 X16 12 1143")
    tran0.writeAction("movir X17 3947")
    tran0.writeAction("slorii X17 X17 12 898")
    tran0.writeAction("slorii X17 X17 12 3082")
    tran0.writeAction("slorii X17 X17 12 1853")
    tran0.writeAction("slorii X17 X17 12 2114")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
