from EFA_v2 import *
def hash_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3013883762751215612, 721950141441849579]
    tran0.writeAction("movir X16 10707")
    tran0.writeAction("slorii X16 X16 12 1909")
    tran0.writeAction("slorii X16 X16 12 97")
    tran0.writeAction("slorii X16 X16 12 425")
    tran0.writeAction("slorii X16 X16 12 2044")
    tran0.writeAction("movir X17 2564")
    tran0.writeAction("slorii X17 X17 12 3613")
    tran0.writeAction("slorii X17 X17 12 1054")
    tran0.writeAction("slorii X17 X17 12 755")
    tran0.writeAction("slorii X17 X17 12 2283")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
