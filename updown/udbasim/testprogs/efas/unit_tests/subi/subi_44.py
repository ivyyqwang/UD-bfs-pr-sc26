from EFA_v2 import *
def subi_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [229158290910537522, -5750]
    tran0.writeAction("movir X16 814")
    tran0.writeAction("slorii X16 X16 12 548")
    tran0.writeAction("slorii X16 X16 12 95")
    tran0.writeAction("slorii X16 X16 12 238")
    tran0.writeAction("slorii X16 X16 12 1842")
    tran0.writeAction("subi X16 X17 -5750")
    tran0.writeAction("yieldt")
    return efa
