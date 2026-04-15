from EFA_v2 import *
def fsub_64_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7065844226328544563, 13492335016093334773]
    tran0.writeAction("movir X16 25102")
    tran0.writeAction("slorii X16 X16 12 3774")
    tran0.writeAction("slorii X16 X16 12 812")
    tran0.writeAction("slorii X16 X16 12 2284")
    tran0.writeAction("slorii X16 X16 12 1331")
    tran0.writeAction("movir X17 47934")
    tran0.writeAction("slorii X17 X17 12 1651")
    tran0.writeAction("slorii X17 X17 12 1584")
    tran0.writeAction("slorii X17 X17 12 3307")
    tran0.writeAction("slorii X17 X17 12 3317")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
