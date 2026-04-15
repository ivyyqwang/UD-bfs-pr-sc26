from EFA_v2 import *
def srsubii_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3599395493933295383, 15, 284]
    tran0.writeAction("movir X16 52748")
    tran0.writeAction("slorii X16 X16 12 1549")
    tran0.writeAction("slorii X16 X16 12 3681")
    tran0.writeAction("slorii X16 X16 12 3949")
    tran0.writeAction("slorii X16 X16 12 2281")
    tran0.writeAction("srsubii X16 X17 15 284")
    tran0.writeAction("yieldt")
    return efa
