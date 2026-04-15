from EFA_v2 import *
def srsubii_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-720078290469498, 1, 1856]
    tran0.writeAction("movir X16 65533")
    tran0.writeAction("slorii X16 X16 12 1809")
    tran0.writeAction("slorii X16 X16 12 1973")
    tran0.writeAction("slorii X16 X16 12 1171")
    tran0.writeAction("slorii X16 X16 12 3462")
    tran0.writeAction("srsubii X16 X17 1 1856")
    tran0.writeAction("yieldt")
    return efa
