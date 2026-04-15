from EFA_v2 import *
def sladdii_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2282393095442838380, 0, 249]
    tran0.writeAction("movir X16 57427")
    tran0.writeAction("slorii X16 X16 12 1273")
    tran0.writeAction("slorii X16 X16 12 644")
    tran0.writeAction("slorii X16 X16 12 1332")
    tran0.writeAction("slorii X16 X16 12 3220")
    tran0.writeAction("sladdii X16 X17 0 249")
    tran0.writeAction("yieldt")
    return efa
