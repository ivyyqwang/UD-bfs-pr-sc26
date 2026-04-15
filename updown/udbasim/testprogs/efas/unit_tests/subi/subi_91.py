from EFA_v2 import *
def subi_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4532636865920441350, 13114]
    tran0.writeAction("movir X16 49432")
    tran0.writeAction("slorii X16 X16 12 3436")
    tran0.writeAction("slorii X16 X16 12 2318")
    tran0.writeAction("slorii X16 X16 12 3982")
    tran0.writeAction("slorii X16 X16 12 1018")
    tran0.writeAction("subi X16 X17 13114")
    tran0.writeAction("yieldt")
    return efa
