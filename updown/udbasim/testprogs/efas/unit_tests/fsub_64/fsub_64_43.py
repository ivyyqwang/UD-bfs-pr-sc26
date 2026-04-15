from EFA_v2 import *
def fsub_64_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9016737166947304760, 1407741964947551028]
    tran0.writeAction("movir X16 32033")
    tran0.writeAction("slorii X16 X16 12 3626")
    tran0.writeAction("slorii X16 X16 12 3644")
    tran0.writeAction("slorii X16 X16 12 3916")
    tran0.writeAction("slorii X16 X16 12 1336")
    tran0.writeAction("movir X17 5001")
    tran0.writeAction("slorii X17 X17 12 1245")
    tran0.writeAction("slorii X17 X17 12 3020")
    tran0.writeAction("slorii X17 X17 12 447")
    tran0.writeAction("slorii X17 X17 12 820")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
