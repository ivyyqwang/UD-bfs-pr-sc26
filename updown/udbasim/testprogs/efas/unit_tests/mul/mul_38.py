from EFA_v2 import *
def mul_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5471496327449889294, -6346313276855022351]
    tran0.writeAction("movir X16 46097")
    tran0.writeAction("slorii X16 X16 12 1393")
    tran0.writeAction("slorii X16 X16 12 1108")
    tran0.writeAction("slorii X16 X16 12 2027")
    tran0.writeAction("slorii X16 X16 12 1522")
    tran0.writeAction("movir X17 42989")
    tran0.writeAction("slorii X17 X17 12 1499")
    tran0.writeAction("slorii X17 X17 12 747")
    tran0.writeAction("slorii X17 X17 12 2912")
    tran0.writeAction("slorii X17 X17 12 3313")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
