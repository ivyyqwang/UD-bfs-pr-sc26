from EFA_v2 import *
def fcnvt_64_32_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4317698799399450452]
    tran0.writeAction("movir X16 15339")
    tran0.writeAction("slorii X16 X16 12 2242")
    tran0.writeAction("slorii X16 X16 12 3729")
    tran0.writeAction("slorii X16 X16 12 1371")
    tran0.writeAction("slorii X16 X16 12 1876")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
