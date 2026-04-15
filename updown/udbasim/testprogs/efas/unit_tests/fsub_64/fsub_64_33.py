from EFA_v2 import *
def fsub_64_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12566682335918281009, 8475347475290028114]
    tran0.writeAction("movir X16 44645")
    tran0.writeAction("slorii X16 X16 12 3376")
    tran0.writeAction("slorii X16 X16 12 221")
    tran0.writeAction("slorii X16 X16 12 2397")
    tran0.writeAction("slorii X16 X16 12 305")
    tran0.writeAction("movir X17 30110")
    tran0.writeAction("slorii X17 X17 12 1977")
    tran0.writeAction("slorii X17 X17 12 4060")
    tran0.writeAction("slorii X17 X17 12 2727")
    tran0.writeAction("slorii X17 X17 12 2130")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
