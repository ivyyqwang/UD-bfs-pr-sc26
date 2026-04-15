from EFA_v2 import *
def mod_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2056977186782206989, -6426388049635541845]
    tran0.writeAction("movir X16 58228")
    tran0.writeAction("slorii X16 X16 12 610")
    tran0.writeAction("slorii X16 X16 12 1438")
    tran0.writeAction("slorii X16 X16 12 3130")
    tran0.writeAction("slorii X16 X16 12 1011")
    tran0.writeAction("movir X17 42704")
    tran0.writeAction("slorii X17 X17 12 3617")
    tran0.writeAction("slorii X17 X17 12 3592")
    tran0.writeAction("slorii X17 X17 12 2695")
    tran0.writeAction("slorii X17 X17 12 3243")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
