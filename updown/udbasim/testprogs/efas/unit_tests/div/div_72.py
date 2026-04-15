from EFA_v2 import *
def div_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4215155144591440570, -6498435938592132203]
    tran0.writeAction("movir X16 50560")
    tran0.writeAction("slorii X16 X16 12 3115")
    tran0.writeAction("slorii X16 X16 12 2709")
    tran0.writeAction("slorii X16 X16 12 1912")
    tran0.writeAction("slorii X16 X16 12 1350")
    tran0.writeAction("movir X17 42448")
    tran0.writeAction("slorii X17 X17 12 3759")
    tran0.writeAction("slorii X17 X17 12 428")
    tran0.writeAction("slorii X17 X17 12 2391")
    tran0.writeAction("slorii X17 X17 12 917")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
