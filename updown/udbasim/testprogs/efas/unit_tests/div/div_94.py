from EFA_v2 import *
def div_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [798485896699411438, -4319573956892766435]
    tran0.writeAction("movir X16 2836")
    tran0.writeAction("slorii X16 X16 12 3243")
    tran0.writeAction("slorii X16 X16 12 326")
    tran0.writeAction("slorii X16 X16 12 3799")
    tran0.writeAction("slorii X16 X16 12 3054")
    tran0.writeAction("movir X17 50189")
    tran0.writeAction("slorii X17 X17 12 3237")
    tran0.writeAction("slorii X17 X17 12 3918")
    tran0.writeAction("slorii X17 X17 12 1548")
    tran0.writeAction("slorii X17 X17 12 3869")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
