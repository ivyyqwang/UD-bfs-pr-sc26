from EFA_v2 import *
def sladdii_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8819243259154252873, 0, 1707]
    tran0.writeAction("movir X16 31332")
    tran0.writeAction("slorii X16 X16 12 1008")
    tran0.writeAction("slorii X16 X16 12 1169")
    tran0.writeAction("slorii X16 X16 12 2652")
    tran0.writeAction("slorii X16 X16 12 1097")
    tran0.writeAction("sladdii X16 X17 0 1707")
    tran0.writeAction("yieldt")
    return efa
