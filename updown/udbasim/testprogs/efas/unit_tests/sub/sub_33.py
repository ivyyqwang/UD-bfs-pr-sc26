from EFA_v2 import *
def sub_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6351425749856735931, 101612039560159066]
    tran0.writeAction("movir X16 22564")
    tran0.writeAction("slorii X16 X16 12 3265")
    tran0.writeAction("slorii X16 X16 12 373")
    tran0.writeAction("slorii X16 X16 12 1965")
    tran0.writeAction("slorii X16 X16 12 699")
    tran0.writeAction("movir X17 360")
    tran0.writeAction("slorii X17 X17 12 4089")
    tran0.writeAction("slorii X17 X17 12 3218")
    tran0.writeAction("slorii X17 X17 12 3629")
    tran0.writeAction("slorii X17 X17 12 3930")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
