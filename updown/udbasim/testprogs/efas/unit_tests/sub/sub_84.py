from EFA_v2 import *
def sub_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1999279219894967120, 5360686335126207840]
    tran0.writeAction("movir X16 7102")
    tran0.writeAction("slorii X16 X16 12 3549")
    tran0.writeAction("slorii X16 X16 12 2972")
    tran0.writeAction("slorii X16 X16 12 2701")
    tran0.writeAction("slorii X16 X16 12 2896")
    tran0.writeAction("movir X17 19044")
    tran0.writeAction("slorii X17 X17 12 4029")
    tran0.writeAction("slorii X17 X17 12 469")
    tran0.writeAction("slorii X17 X17 12 1999")
    tran0.writeAction("slorii X17 X17 12 3424")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
