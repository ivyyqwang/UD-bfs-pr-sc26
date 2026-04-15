from EFA_v2 import *
def sub_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3548730790645153564, -8177628776981349965]
    tran0.writeAction("movir X16 52928")
    tran0.writeAction("slorii X16 X16 12 1538")
    tran0.writeAction("slorii X16 X16 12 1500")
    tran0.writeAction("slorii X16 X16 12 428")
    tran0.writeAction("slorii X16 X16 12 228")
    tran0.writeAction("movir X17 36483")
    tran0.writeAction("slorii X17 X17 12 927")
    tran0.writeAction("slorii X17 X17 12 1099")
    tran0.writeAction("slorii X17 X17 12 59")
    tran0.writeAction("slorii X17 X17 12 2483")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
