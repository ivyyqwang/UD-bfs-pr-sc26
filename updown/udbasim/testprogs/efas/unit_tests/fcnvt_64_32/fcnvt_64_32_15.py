from EFA_v2 import *
def fcnvt_64_32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14055389855385386900]
    tran0.writeAction("movir X16 49934")
    tran0.writeAction("slorii X16 X16 12 3177")
    tran0.writeAction("slorii X16 X16 12 2773")
    tran0.writeAction("slorii X16 X16 12 3583")
    tran0.writeAction("slorii X16 X16 12 3988")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
