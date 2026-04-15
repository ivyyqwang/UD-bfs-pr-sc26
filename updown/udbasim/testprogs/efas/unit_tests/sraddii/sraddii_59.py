from EFA_v2 import *
def sraddii_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4236784988177577279, 6, 1821]
    tran0.writeAction("movir X16 50483")
    tran0.writeAction("slorii X16 X16 12 3752")
    tran0.writeAction("slorii X16 X16 12 45")
    tran0.writeAction("slorii X16 X16 12 3964")
    tran0.writeAction("slorii X16 X16 12 2753")
    tran0.writeAction("sraddii X16 X17 6 1821")
    tran0.writeAction("yieldt")
    return efa
