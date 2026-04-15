from EFA_v2 import *
def addi_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-201842701219897728, 17363]
    tran0.writeAction("movir X16 64818")
    tran0.writeAction("slorii X16 X16 12 3730")
    tran0.writeAction("slorii X16 X16 12 501")
    tran0.writeAction("slorii X16 X16 12 1157")
    tran0.writeAction("slorii X16 X16 12 3712")
    tran0.writeAction("addi X16 X17 17363")
    tran0.writeAction("yieldt")
    return efa
