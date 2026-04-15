from EFA_v2 import *
def add_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5088129611829937341, 3437220884259417053]
    tran0.writeAction("movir X16 18076")
    tran0.writeAction("slorii X16 X16 12 2734")
    tran0.writeAction("slorii X16 X16 12 3204")
    tran0.writeAction("slorii X16 X16 12 1104")
    tran0.writeAction("slorii X16 X16 12 1213")
    tran0.writeAction("movir X17 12211")
    tran0.writeAction("slorii X17 X17 12 1890")
    tran0.writeAction("slorii X17 X17 12 3804")
    tran0.writeAction("slorii X17 X17 12 3426")
    tran0.writeAction("slorii X17 X17 12 3037")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
