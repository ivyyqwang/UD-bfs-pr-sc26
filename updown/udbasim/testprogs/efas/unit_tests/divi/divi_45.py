from EFA_v2 import *
def divi_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8295663601284324046, -6665]
    tran0.writeAction("movir X16 29472")
    tran0.writeAction("slorii X16 X16 12 481")
    tran0.writeAction("slorii X16 X16 12 2002")
    tran0.writeAction("slorii X16 X16 12 2825")
    tran0.writeAction("slorii X16 X16 12 2766")
    tran0.writeAction("divi X16 X17 -6665")
    tran0.writeAction("yieldt")
    return efa
