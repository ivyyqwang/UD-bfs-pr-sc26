from EFA_v2 import *
def mod_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2041914876444028757, 7032492469199578859]
    tran0.writeAction("movir X16 58281")
    tran0.writeAction("slorii X16 X16 12 2707")
    tran0.writeAction("slorii X16 X16 12 3335")
    tran0.writeAction("slorii X16 X16 12 3965")
    tran0.writeAction("slorii X16 X16 12 171")
    tran0.writeAction("movir X17 24984")
    tran0.writeAction("slorii X17 X17 12 1770")
    tran0.writeAction("slorii X17 X17 12 1048")
    tran0.writeAction("slorii X17 X17 12 1026")
    tran0.writeAction("slorii X17 X17 12 1771")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
