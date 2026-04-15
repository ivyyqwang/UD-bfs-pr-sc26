from EFA_v2 import *
def sub_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-164654963748150349, -4844305211163049765]
    tran0.writeAction("movir X16 64951")
    tran0.writeAction("slorii X16 X16 12 114")
    tran0.writeAction("slorii X16 X16 12 3791")
    tran0.writeAction("slorii X16 X16 12 1174")
    tran0.writeAction("slorii X16 X16 12 947")
    tran0.writeAction("movir X17 48325")
    tran0.writeAction("slorii X17 X17 12 2337")
    tran0.writeAction("slorii X17 X17 12 929")
    tran0.writeAction("slorii X17 X17 12 216")
    tran0.writeAction("slorii X17 X17 12 219")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
