from EFA_v2 import *
def div_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7329098321569165018, 1561607402283534039]
    tran0.writeAction("movir X16 39497")
    tran0.writeAction("slorii X16 X16 12 3326")
    tran0.writeAction("slorii X16 X16 12 2146")
    tran0.writeAction("slorii X16 X16 12 3925")
    tran0.writeAction("slorii X16 X16 12 294")
    tran0.writeAction("movir X17 5547")
    tran0.writeAction("slorii X17 X17 12 3866")
    tran0.writeAction("slorii X17 X17 12 2203")
    tran0.writeAction("slorii X17 X17 12 2992")
    tran0.writeAction("slorii X17 X17 12 1751")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
