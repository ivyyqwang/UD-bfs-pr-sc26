from EFA_v2 import *
def div_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1572098077645148522, 641270634696066467]
    tran0.writeAction("movir X16 5585")
    tran0.writeAction("slorii X16 X16 12 877")
    tran0.writeAction("slorii X16 X16 12 3918")
    tran0.writeAction("slorii X16 X16 12 465")
    tran0.writeAction("slorii X16 X16 12 362")
    tran0.writeAction("movir X17 2278")
    tran0.writeAction("slorii X17 X17 12 1027")
    tran0.writeAction("slorii X17 X17 12 3745")
    tran0.writeAction("slorii X17 X17 12 3884")
    tran0.writeAction("slorii X17 X17 12 1443")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
