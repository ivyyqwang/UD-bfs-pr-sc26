from EFA_v2 import *
def div_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1610540445180862318, 4387059765329736425]
    tran0.writeAction("movir X16 5721")
    tran0.writeAction("slorii X16 X16 12 3232")
    tran0.writeAction("slorii X16 X16 12 123")
    tran0.writeAction("slorii X16 X16 12 1657")
    tran0.writeAction("slorii X16 X16 12 3950")
    tran0.writeAction("movir X17 15585")
    tran0.writeAction("slorii X17 X17 12 3961")
    tran0.writeAction("slorii X17 X17 12 3304")
    tran0.writeAction("slorii X17 X17 12 3635")
    tran0.writeAction("slorii X17 X17 12 745")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
