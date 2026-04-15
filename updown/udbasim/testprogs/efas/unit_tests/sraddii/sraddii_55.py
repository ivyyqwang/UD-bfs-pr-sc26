from EFA_v2 import *
def sraddii_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8371668508088494928, 8, 1748]
    tran0.writeAction("movir X16 35793")
    tran0.writeAction("slorii X16 X16 12 3517")
    tran0.writeAction("slorii X16 X16 12 2254")
    tran0.writeAction("slorii X16 X16 12 249")
    tran0.writeAction("slorii X16 X16 12 1200")
    tran0.writeAction("sraddii X16 X17 8 1748")
    tran0.writeAction("yieldt")
    return efa
