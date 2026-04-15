from EFA_v2 import *
def sub_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3595562311010891115, 6733055629910363922]
    tran0.writeAction("movir X16 12774")
    tran0.writeAction("slorii X16 X16 12 13")
    tran0.writeAction("slorii X16 X16 12 3883")
    tran0.writeAction("slorii X16 X16 12 2403")
    tran0.writeAction("slorii X16 X16 12 1387")
    tran0.writeAction("movir X17 23920")
    tran0.writeAction("slorii X17 X17 12 2534")
    tran0.writeAction("slorii X17 X17 12 3089")
    tran0.writeAction("slorii X17 X17 12 3076")
    tran0.writeAction("slorii X17 X17 12 3858")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
