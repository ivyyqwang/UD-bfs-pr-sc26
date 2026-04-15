from EFA_v2 import *
def mod_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4626364571998221712, 9185852806167136139]
    tran0.writeAction("movir X16 16436")
    tran0.writeAction("slorii X16 X16 12 609")
    tran0.writeAction("slorii X16 X16 12 275")
    tran0.writeAction("slorii X16 X16 12 1663")
    tran0.writeAction("slorii X16 X16 12 1424")
    tran0.writeAction("movir X17 32634")
    tran0.writeAction("slorii X17 X17 12 2887")
    tran0.writeAction("slorii X17 X17 12 1374")
    tran0.writeAction("slorii X17 X17 12 2528")
    tran0.writeAction("slorii X17 X17 12 1931")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
