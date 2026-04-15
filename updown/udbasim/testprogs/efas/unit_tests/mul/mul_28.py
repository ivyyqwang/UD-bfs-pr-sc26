from EFA_v2 import *
def mul_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3122199875646063247, -5559029230371797677]
    tran0.writeAction("movir X16 54443")
    tran0.writeAction("slorii X16 X16 12 2940")
    tran0.writeAction("slorii X16 X16 12 342")
    tran0.writeAction("slorii X16 X16 12 1423")
    tran0.writeAction("slorii X16 X16 12 3441")
    tran0.writeAction("movir X17 45786")
    tran0.writeAction("slorii X17 X17 12 1477")
    tran0.writeAction("slorii X17 X17 12 3635")
    tran0.writeAction("slorii X17 X17 12 2768")
    tran0.writeAction("slorii X17 X17 12 1363")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
