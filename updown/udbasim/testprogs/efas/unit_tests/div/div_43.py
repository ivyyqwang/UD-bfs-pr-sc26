from EFA_v2 import *
def div_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2522170372260165190, 7819799694790289973]
    tran0.writeAction("movir X16 8960")
    tran0.writeAction("slorii X16 X16 12 2249")
    tran0.writeAction("slorii X16 X16 12 1837")
    tran0.writeAction("slorii X16 X16 12 2383")
    tran0.writeAction("slorii X16 X16 12 1606")
    tran0.writeAction("movir X17 27781")
    tran0.writeAction("slorii X17 X17 12 2086")
    tran0.writeAction("slorii X17 X17 12 1070")
    tran0.writeAction("slorii X17 X17 12 2798")
    tran0.writeAction("slorii X17 X17 12 2613")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
