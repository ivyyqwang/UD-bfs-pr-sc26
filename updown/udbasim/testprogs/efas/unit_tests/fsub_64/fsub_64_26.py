from EFA_v2 import *
def fsub_64_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4338128842676116783, 6532613154881905693]
    tran0.writeAction("movir X16 15412")
    tran0.writeAction("slorii X16 X16 12 531")
    tran0.writeAction("slorii X16 X16 12 689")
    tran0.writeAction("slorii X16 X16 12 2401")
    tran0.writeAction("slorii X16 X16 12 3375")
    tran0.writeAction("movir X17 23208")
    tran0.writeAction("slorii X17 X17 12 2064")
    tran0.writeAction("slorii X17 X17 12 3479")
    tran0.writeAction("slorii X17 X17 12 3194")
    tran0.writeAction("slorii X17 X17 12 1053")
    tran0.writeAction("fsub.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
