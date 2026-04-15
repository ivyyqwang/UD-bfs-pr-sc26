from EFA_v2 import *
def srsubii_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7880437780744769975, 15, 401]
    tran0.writeAction("movir X16 27996")
    tran0.writeAction("slorii X16 X16 12 3846")
    tran0.writeAction("slorii X16 X16 12 2243")
    tran0.writeAction("slorii X16 X16 12 3521")
    tran0.writeAction("slorii X16 X16 12 439")
    tran0.writeAction("srsubii X16 X17 15 401")
    tran0.writeAction("yieldt")
    return efa
