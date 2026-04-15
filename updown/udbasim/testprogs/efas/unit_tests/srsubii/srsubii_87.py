from EFA_v2 import *
def srsubii_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1168231206745761258, 12, 507]
    tran0.writeAction("movir X16 4150")
    tran0.writeAction("slorii X16 X16 12 1601")
    tran0.writeAction("slorii X16 X16 12 1997")
    tran0.writeAction("slorii X16 X16 12 2486")
    tran0.writeAction("slorii X16 X16 12 1514")
    tran0.writeAction("srsubii X16 X17 12 507")
    tran0.writeAction("yieldt")
    return efa
