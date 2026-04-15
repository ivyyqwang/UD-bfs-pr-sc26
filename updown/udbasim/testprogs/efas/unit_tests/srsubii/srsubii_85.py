from EFA_v2 import *
def srsubii_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-256929555718720454, 9, 1471]
    tran0.writeAction("movir X16 64623")
    tran0.writeAction("slorii X16 X16 12 830")
    tran0.writeAction("slorii X16 X16 12 3627")
    tran0.writeAction("slorii X16 X16 12 355")
    tran0.writeAction("slorii X16 X16 12 1082")
    tran0.writeAction("srsubii X16 X17 9 1471")
    tran0.writeAction("yieldt")
    return efa
