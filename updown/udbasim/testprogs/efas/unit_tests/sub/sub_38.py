from EFA_v2 import *
def sub_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7626624784491473279, -5941029064060698561]
    tran0.writeAction("movir X16 38440")
    tran0.writeAction("slorii X16 X16 12 3218")
    tran0.writeAction("slorii X16 X16 12 2693")
    tran0.writeAction("slorii X16 X16 12 801")
    tran0.writeAction("slorii X16 X16 12 1665")
    tran0.writeAction("movir X17 44429")
    tran0.writeAction("slorii X17 X17 12 920")
    tran0.writeAction("slorii X17 X17 12 2828")
    tran0.writeAction("slorii X17 X17 12 1600")
    tran0.writeAction("slorii X17 X17 12 63")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
