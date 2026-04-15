from EFA_v2 import *
def fsub_32_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1361072973, 2913339184]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 81")
    tran0.writeAction("slorii X16 X16 12 517")
    tran0.writeAction("slorii X16 X16 12 845")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 173")
    tran0.writeAction("slorii X17 X17 12 2656")
    tran0.writeAction("slorii X17 X17 12 1840")
    tran0.writeAction("fsub.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
