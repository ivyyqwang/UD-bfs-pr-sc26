from EFA_v2 import *
def modi_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4462381768746830302, -2875]
    tran0.writeAction("movir X16 15853")
    tran0.writeAction("slorii X16 X16 12 2313")
    tran0.writeAction("slorii X16 X16 12 882")
    tran0.writeAction("slorii X16 X16 12 1368")
    tran0.writeAction("slorii X16 X16 12 2526")
    tran0.writeAction("modi X16 X17 -2875")
    tran0.writeAction("yieldt")
    return efa
