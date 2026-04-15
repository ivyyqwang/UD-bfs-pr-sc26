from EFA_v2 import *
def subi_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7410374949050692231, 354]
    tran0.writeAction("movir X16 26326")
    tran0.writeAction("slorii X16 X16 12 3852")
    tran0.writeAction("slorii X16 X16 12 282")
    tran0.writeAction("slorii X16 X16 12 2539")
    tran0.writeAction("slorii X16 X16 12 647")
    tran0.writeAction("subi X16 X17 354")
    tran0.writeAction("yieldt")
    return efa
