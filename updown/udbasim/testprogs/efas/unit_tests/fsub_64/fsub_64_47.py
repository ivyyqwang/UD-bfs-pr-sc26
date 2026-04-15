from EFA_v2 import *
def fsub_64_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14254353336200310986, 13631076743620569677]
    tran0.writeAction("movir X16 50641")
    tran0.writeAction("slorii X16 X16 12 2605")
    tran0.writeAction("slorii X16 X16 12 1571")
    tran0.writeAction("slorii X16 X16 12 507")
    tran0.writeAction("slorii X16 X16 12 202")
    tran0.writeAction("movir X17 48427")
    tran0.writeAction("slorii X17 X17 12 1281")
    tran0.writeAction("slorii X17 X17 12 1001")
    tran0.writeAction("slorii X17 X17 12 2426")
    tran0.writeAction("slorii X17 X17 12 2637")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
