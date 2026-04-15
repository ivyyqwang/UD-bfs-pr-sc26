from EFA_v2 import *
def muli_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4386907873585459135, -6167]
    tran0.writeAction("movir X16 15585")
    tran0.writeAction("slorii X16 X16 12 1751")
    tran0.writeAction("slorii X16 X16 12 2011")
    tran0.writeAction("slorii X16 X16 12 1742")
    tran0.writeAction("slorii X16 X16 12 4031")
    tran0.writeAction("muli X16 X17 -6167")
    tran0.writeAction("yieldt")
    return efa
