from EFA_v2 import *
def slsubii_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [661613431965426424, 0, 1476]
    tran0.writeAction("movir X16 2350")
    tran0.writeAction("slorii X16 X16 12 2142")
    tran0.writeAction("slorii X16 X16 12 2358")
    tran0.writeAction("slorii X16 X16 12 3794")
    tran0.writeAction("slorii X16 X16 12 760")
    tran0.writeAction("slsubii X16 X17 0 1476")
    tran0.writeAction("yieldt")
    return efa
