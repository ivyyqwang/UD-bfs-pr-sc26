from EFA_v2 import *
def div_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7123303667995198362, 330091927906951025]
    tran0.writeAction("movir X16 25307")
    tran0.writeAction("slorii X16 X16 12 239")
    tran0.writeAction("slorii X16 X16 12 502")
    tran0.writeAction("slorii X16 X16 12 372")
    tran0.writeAction("slorii X16 X16 12 922")
    tran0.writeAction("movir X17 1172")
    tran0.writeAction("slorii X17 X17 12 2957")
    tran0.writeAction("slorii X17 X17 12 3082")
    tran0.writeAction("slorii X17 X17 12 481")
    tran0.writeAction("slorii X17 X17 12 3953")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
