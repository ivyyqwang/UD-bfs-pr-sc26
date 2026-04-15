from EFA_v2 import *
def slsubii_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2984372805452757173, 8, 1255]
    tran0.writeAction("movir X16 10602")
    tran0.writeAction("slorii X16 X16 12 2548")
    tran0.writeAction("slorii X16 X16 12 306")
    tran0.writeAction("slorii X16 X16 12 1423")
    tran0.writeAction("slorii X16 X16 12 2229")
    tran0.writeAction("slsubii X16 X17 8 1255")
    tran0.writeAction("yieldt")
    return efa
