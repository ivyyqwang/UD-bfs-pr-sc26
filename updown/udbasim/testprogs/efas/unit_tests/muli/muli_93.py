from EFA_v2 import *
def muli_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5809071661452247391, -28036]
    tran0.writeAction("movir X16 20637")
    tran0.writeAction("slorii X16 X16 12 3966")
    tran0.writeAction("slorii X16 X16 12 1527")
    tran0.writeAction("slorii X16 X16 12 2660")
    tran0.writeAction("slorii X16 X16 12 351")
    tran0.writeAction("muli X16 X17 -28036")
    tran0.writeAction("yieldt")
    return efa
