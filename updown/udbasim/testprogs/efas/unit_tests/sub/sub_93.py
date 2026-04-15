from EFA_v2 import *
def sub_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7063211621158853250, -3376854791468108641]
    tran0.writeAction("movir X16 25093")
    tran0.writeAction("slorii X16 X16 12 2328")
    tran0.writeAction("slorii X16 X16 12 3076")
    tran0.writeAction("slorii X16 X16 12 2393")
    tran0.writeAction("slorii X16 X16 12 2690")
    tran0.writeAction("movir X17 53539")
    tran0.writeAction("slorii X17 X17 12 7")
    tran0.writeAction("slorii X17 X17 12 1376")
    tran0.writeAction("slorii X17 X17 12 1915")
    tran0.writeAction("slorii X17 X17 12 1183")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
