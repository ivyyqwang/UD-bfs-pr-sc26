from EFA_v2 import *
def muli_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6668783583117792469, -32656]
    tran0.writeAction("movir X16 23692")
    tran0.writeAction("slorii X16 X16 12 1141")
    tran0.writeAction("slorii X16 X16 12 1547")
    tran0.writeAction("slorii X16 X16 12 2837")
    tran0.writeAction("slorii X16 X16 12 1237")
    tran0.writeAction("muli X16 X17 -32656")
    tran0.writeAction("yieldt")
    return efa
