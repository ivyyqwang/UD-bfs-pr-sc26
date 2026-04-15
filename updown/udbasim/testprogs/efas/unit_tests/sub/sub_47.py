from EFA_v2 import *
def sub_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1694424786060759329, -4558002901939681920]
    tran0.writeAction("movir X16 59516")
    tran0.writeAction("slorii X16 X16 12 794")
    tran0.writeAction("slorii X16 X16 12 624")
    tran0.writeAction("slorii X16 X16 12 946")
    tran0.writeAction("slorii X16 X16 12 3807")
    tran0.writeAction("movir X17 49342")
    tran0.writeAction("slorii X17 X17 12 2952")
    tran0.writeAction("slorii X17 X17 12 656")
    tran0.writeAction("slorii X17 X17 12 2808")
    tran0.writeAction("slorii X17 X17 12 1408")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
