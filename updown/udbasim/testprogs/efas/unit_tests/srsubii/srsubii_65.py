from EFA_v2 import *
def srsubii_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [248826349395839166, 15, 1387]
    tran0.writeAction("movir X16 884")
    tran0.writeAction("slorii X16 X16 12 35")
    tran0.writeAction("slorii X16 X16 12 3862")
    tran0.writeAction("slorii X16 X16 12 2032")
    tran0.writeAction("slorii X16 X16 12 2238")
    tran0.writeAction("srsubii X16 X17 15 1387")
    tran0.writeAction("yieldt")
    return efa
