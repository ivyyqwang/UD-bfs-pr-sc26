from EFA_v2 import *
def fsub_32_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2659356646, 3137990141]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 158")
    tran0.writeAction("slorii X16 X16 12 2088")
    tran0.writeAction("slorii X16 X16 12 4070")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 187")
    tran0.writeAction("slorii X17 X17 12 158")
    tran0.writeAction("slorii X17 X17 12 3581")
    tran0.writeAction("fsub.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
