from EFA_v2 import *
def sraddii_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5005878918971001998, 9, 1257]
    tran0.writeAction("movir X16 47751")
    tran0.writeAction("slorii X16 X16 12 2234")
    tran0.writeAction("slorii X16 X16 12 1342")
    tran0.writeAction("slorii X16 X16 12 479")
    tran0.writeAction("slorii X16 X16 12 882")
    tran0.writeAction("sraddii X16 X17 9 1257")
    tran0.writeAction("yieldt")
    return efa
