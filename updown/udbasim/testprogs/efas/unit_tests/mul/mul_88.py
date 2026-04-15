from EFA_v2 import *
def mul_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9157032351814984222, -2424195853659831186]
    tran0.writeAction("movir X16 33003")
    tran0.writeAction("slorii X16 X16 12 2809")
    tran0.writeAction("slorii X16 X16 12 1937")
    tran0.writeAction("slorii X16 X16 12 1261")
    tran0.writeAction("slorii X16 X16 12 3554")
    tran0.writeAction("movir X17 56923")
    tran0.writeAction("slorii X17 X17 12 2155")
    tran0.writeAction("slorii X17 X17 12 1804")
    tran0.writeAction("slorii X17 X17 12 2584")
    tran0.writeAction("slorii X17 X17 12 1134")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
