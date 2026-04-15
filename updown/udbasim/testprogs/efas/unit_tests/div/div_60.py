from EFA_v2 import *
def div_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4346223954853608400, -8281178089351386037]
    tran0.writeAction("movir X16 15440")
    tran0.writeAction("slorii X16 X16 12 3642")
    tran0.writeAction("slorii X16 X16 12 2271")
    tran0.writeAction("slorii X16 X16 12 1403")
    tran0.writeAction("slorii X16 X16 12 3024")
    tran0.writeAction("movir X17 36115")
    tran0.writeAction("slorii X17 X17 12 1414")
    tran0.writeAction("slorii X17 X17 12 1854")
    tran0.writeAction("slorii X17 X17 12 1894")
    tran0.writeAction("slorii X17 X17 12 3147")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
