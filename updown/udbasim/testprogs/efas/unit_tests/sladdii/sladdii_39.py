from EFA_v2 import *
def sladdii_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6718362089448204701, 13, 732]
    tran0.writeAction("movir X16 23868")
    tran0.writeAction("slorii X16 X16 12 1707")
    tran0.writeAction("slorii X16 X16 12 2454")
    tran0.writeAction("slorii X16 X16 12 46")
    tran0.writeAction("slorii X16 X16 12 2461")
    tran0.writeAction("sladdii X16 X17 13 732")
    tran0.writeAction("yieldt")
    return efa
