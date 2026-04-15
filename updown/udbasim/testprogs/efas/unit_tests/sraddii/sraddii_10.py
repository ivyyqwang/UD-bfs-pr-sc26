from EFA_v2 import *
def sraddii_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5559788269967373336, 1, 1641]
    tran0.writeAction("movir X16 45783")
    tran0.writeAction("slorii X16 X16 12 2720")
    tran0.writeAction("slorii X16 X16 12 1670")
    tran0.writeAction("slorii X16 X16 12 864")
    tran0.writeAction("slorii X16 X16 12 3048")
    tran0.writeAction("sraddii X16 X17 1 1641")
    tran0.writeAction("yieldt")
    return efa
