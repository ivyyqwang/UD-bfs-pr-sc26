from EFA_v2 import *
def sraddii_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-15120927445292114, 11, 2008]
    tran0.writeAction("movir X16 65482")
    tran0.writeAction("slorii X16 X16 12 1145")
    tran0.writeAction("slorii X16 X16 12 2234")
    tran0.writeAction("slorii X16 X16 12 3886")
    tran0.writeAction("slorii X16 X16 12 2990")
    tran0.writeAction("sraddii X16 X17 11 2008")
    tran0.writeAction("yieldt")
    return efa
