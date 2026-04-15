from EFA_v2 import *
def sub_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5773041057467896286, 2736194237617902045]
    tran0.writeAction("movir X16 20509")
    tran0.writeAction("slorii X16 X16 12 3940")
    tran0.writeAction("slorii X16 X16 12 320")
    tran0.writeAction("slorii X16 X16 12 489")
    tran0.writeAction("slorii X16 X16 12 478")
    tran0.writeAction("movir X17 9720")
    tran0.writeAction("slorii X17 X17 12 3746")
    tran0.writeAction("slorii X17 X17 12 2433")
    tran0.writeAction("slorii X17 X17 12 2809")
    tran0.writeAction("slorii X17 X17 12 477")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
