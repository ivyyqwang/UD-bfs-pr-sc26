from EFA_v2 import *
def div_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1388803050134516258, 4751140484600151600]
    tran0.writeAction("movir X16 60601")
    tran0.writeAction("slorii X16 X16 12 4015")
    tran0.writeAction("slorii X16 X16 12 3053")
    tran0.writeAction("slorii X16 X16 12 3084")
    tran0.writeAction("slorii X16 X16 12 3550")
    tran0.writeAction("movir X17 16879")
    tran0.writeAction("slorii X17 X17 12 1809")
    tran0.writeAction("slorii X17 X17 12 2334")
    tran0.writeAction("slorii X17 X17 12 2331")
    tran0.writeAction("slorii X17 X17 12 3632")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
