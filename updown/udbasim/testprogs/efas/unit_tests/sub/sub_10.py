from EFA_v2 import *
def sub_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5826618008197956060, 8523446085978195845]
    tran0.writeAction("movir X16 44835")
    tran0.writeAction("slorii X16 X16 12 2844")
    tran0.writeAction("slorii X16 X16 12 2771")
    tran0.writeAction("slorii X16 X16 12 1911")
    tran0.writeAction("slorii X16 X16 12 3620")
    tran0.writeAction("movir X17 30281")
    tran0.writeAction("slorii X17 X17 12 1488")
    tran0.writeAction("slorii X17 X17 12 3672")
    tran0.writeAction("slorii X17 X17 12 3784")
    tran0.writeAction("slorii X17 X17 12 1925")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
