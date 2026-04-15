from EFA_v2 import *
def div_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4356721481546156418, 3073834164625693050]
    tran0.writeAction("movir X16 50057")
    tran0.writeAction("slorii X16 X16 12 3342")
    tran0.writeAction("slorii X16 X16 12 1339")
    tran0.writeAction("slorii X16 X16 12 523")
    tran0.writeAction("slorii X16 X16 12 1662")
    tran0.writeAction("movir X17 10920")
    tran0.writeAction("slorii X17 X17 12 1854")
    tran0.writeAction("slorii X17 X17 12 776")
    tran0.writeAction("slorii X17 X17 12 3989")
    tran0.writeAction("slorii X17 X17 12 2426")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
