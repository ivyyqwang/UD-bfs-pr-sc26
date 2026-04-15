from EFA_v2 import *
def sraddii_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4290302517847587055, 10, 859]
    tran0.writeAction("movir X16 50293")
    tran0.writeAction("slorii X16 X16 12 3209")
    tran0.writeAction("slorii X16 X16 12 1868")
    tran0.writeAction("slorii X16 X16 12 2992")
    tran0.writeAction("slorii X16 X16 12 1809")
    tran0.writeAction("sraddii X16 X17 10 859")
    tran0.writeAction("yieldt")
    return efa
