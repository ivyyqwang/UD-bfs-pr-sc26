from EFA_v2 import *
def div_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6021973365488080657, -4747597038058476141]
    tran0.writeAction("movir X16 44141")
    tran0.writeAction("slorii X16 X16 12 2674")
    tran0.writeAction("slorii X16 X16 12 319")
    tran0.writeAction("slorii X16 X16 12 898")
    tran0.writeAction("slorii X16 X16 12 2287")
    tran0.writeAction("movir X17 48669")
    tran0.writeAction("slorii X17 X17 12 602")
    tran0.writeAction("slorii X17 X17 12 1489")
    tran0.writeAction("slorii X17 X17 12 3390")
    tran0.writeAction("slorii X17 X17 12 3475")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
