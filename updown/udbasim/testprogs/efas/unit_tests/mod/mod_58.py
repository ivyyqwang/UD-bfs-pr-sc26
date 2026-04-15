from EFA_v2 import *
def mod_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1281743891543514793, 6341561012502526577]
    tran0.writeAction("movir X16 4553")
    tran0.writeAction("slorii X16 X16 12 2740")
    tran0.writeAction("slorii X16 X16 12 1860")
    tran0.writeAction("slorii X16 X16 12 1957")
    tran0.writeAction("slorii X16 X16 12 3753")
    tran0.writeAction("movir X17 22529")
    tran0.writeAction("slorii X17 X17 12 3074")
    tran0.writeAction("slorii X17 X17 12 1103")
    tran0.writeAction("slorii X17 X17 12 2783")
    tran0.writeAction("slorii X17 X17 12 2673")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
