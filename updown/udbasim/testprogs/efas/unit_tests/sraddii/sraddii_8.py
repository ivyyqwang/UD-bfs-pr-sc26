from EFA_v2 import *
def sraddii_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8198106087575424663, 7, 430]
    tran0.writeAction("movir X16 36410")
    tran0.writeAction("slorii X16 X16 12 1951")
    tran0.writeAction("slorii X16 X16 12 739")
    tran0.writeAction("slorii X16 X16 12 407")
    tran0.writeAction("slorii X16 X16 12 361")
    tran0.writeAction("sraddii X16 X17 7 430")
    tran0.writeAction("yieldt")
    return efa
