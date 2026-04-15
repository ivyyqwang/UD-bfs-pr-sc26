from EFA_v2 import *
def subi_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3351738213010214573, 11065]
    tran0.writeAction("movir X16 11907")
    tran0.writeAction("slorii X16 X16 12 3138")
    tran0.writeAction("slorii X16 X16 12 1406")
    tran0.writeAction("slorii X16 X16 12 2360")
    tran0.writeAction("slorii X16 X16 12 3757")
    tran0.writeAction("subi X16 X17 11065")
    tran0.writeAction("yieldt")
    return efa
