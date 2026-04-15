from EFA_v2 import *
def fsub_64_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [873020375789568194, 16694578957988495381]
    tran0.writeAction("movir X16 3101")
    tran0.writeAction("slorii X16 X16 12 2422")
    tran0.writeAction("slorii X16 X16 12 2052")
    tran0.writeAction("slorii X16 X16 12 2520")
    tran0.writeAction("slorii X16 X16 12 194")
    tran0.writeAction("movir X17 59311")
    tran0.writeAction("slorii X17 X17 12 241")
    tran0.writeAction("slorii X17 X17 12 3153")
    tran0.writeAction("slorii X17 X17 12 2520")
    tran0.writeAction("slorii X17 X17 12 21")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
