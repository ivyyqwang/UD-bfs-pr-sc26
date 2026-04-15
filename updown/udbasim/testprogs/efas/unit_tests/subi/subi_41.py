from EFA_v2 import *
def subi_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1990996944647198414, 32433]
    tran0.writeAction("movir X16 7073")
    tran0.writeAction("slorii X16 X16 12 1810")
    tran0.writeAction("slorii X16 X16 12 3106")
    tran0.writeAction("slorii X16 X16 12 2393")
    tran0.writeAction("slorii X16 X16 12 1742")
    tran0.writeAction("subi X16 X17 32433")
    tran0.writeAction("yieldt")
    return efa
