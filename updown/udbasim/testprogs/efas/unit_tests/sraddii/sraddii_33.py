from EFA_v2 import *
def sraddii_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5087502217787471341, 14, 885]
    tran0.writeAction("movir X16 18074")
    tran0.writeAction("slorii X16 X16 12 1796")
    tran0.writeAction("slorii X16 X16 12 4085")
    tran0.writeAction("slorii X16 X16 12 959")
    tran0.writeAction("slorii X16 X16 12 1517")
    tran0.writeAction("sraddii X16 X17 14 885")
    tran0.writeAction("yieldt")
    return efa
