from EFA_v2 import *
def div_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-668380133035317832, 6467837632699095605]
    tran0.writeAction("movir X16 63161")
    tran0.writeAction("slorii X16 X16 12 1788")
    tran0.writeAction("slorii X16 X16 12 3947")
    tran0.writeAction("slorii X16 X16 12 2054")
    tran0.writeAction("slorii X16 X16 12 1464")
    tran0.writeAction("movir X17 22978")
    tran0.writeAction("slorii X17 X17 12 1536")
    tran0.writeAction("slorii X17 X17 12 3857")
    tran0.writeAction("slorii X17 X17 12 3821")
    tran0.writeAction("slorii X17 X17 12 2613")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
