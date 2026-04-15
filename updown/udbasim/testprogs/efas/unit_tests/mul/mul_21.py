from EFA_v2 import *
def mul_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1288530408779927204, 8468762555554842481]
    tran0.writeAction("movir X16 4577")
    tran0.writeAction("slorii X16 X16 12 3193")
    tran0.writeAction("slorii X16 X16 12 1137")
    tran0.writeAction("slorii X16 X16 12 2524")
    tran0.writeAction("slorii X16 X16 12 3748")
    tran0.writeAction("movir X17 30087")
    tran0.writeAction("slorii X17 X17 12 362")
    tran0.writeAction("slorii X17 X17 12 3266")
    tran0.writeAction("slorii X17 X17 12 3996")
    tran0.writeAction("slorii X17 X17 12 1905")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
