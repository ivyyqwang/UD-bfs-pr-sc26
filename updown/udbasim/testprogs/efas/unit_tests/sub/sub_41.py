from EFA_v2 import *
def sub_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4063804174746327866, 1075836919916393840]
    tran0.writeAction("movir X16 51098")
    tran0.writeAction("slorii X16 X16 12 1914")
    tran0.writeAction("slorii X16 X16 12 591")
    tran0.writeAction("slorii X16 X16 12 2030")
    tran0.writeAction("slorii X16 X16 12 1222")
    tran0.writeAction("movir X17 3822")
    tran0.writeAction("slorii X17 X17 12 575")
    tran0.writeAction("slorii X17 X17 12 2695")
    tran0.writeAction("slorii X17 X17 12 3551")
    tran0.writeAction("slorii X17 X17 12 1392")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
