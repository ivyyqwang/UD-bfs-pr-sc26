from EFA_v2 import *
def divi_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-110536379114909370, -10031]
    tran0.writeAction("movir X16 65143")
    tran0.writeAction("slorii X16 X16 12 1211")
    tran0.writeAction("slorii X16 X16 12 4020")
    tran0.writeAction("slorii X16 X16 12 401")
    tran0.writeAction("slorii X16 X16 12 326")
    tran0.writeAction("divi X16 X17 -10031")
    tran0.writeAction("yieldt")
    return efa
