from EFA_v2 import *
def sraddii_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8785059198871827950, 12, 1302]
    tran0.writeAction("movir X16 34325")
    tran0.writeAction("slorii X16 X16 12 819")
    tran0.writeAction("slorii X16 X16 12 1072")
    tran0.writeAction("slorii X16 X16 12 1912")
    tran0.writeAction("slorii X16 X16 12 2578")
    tran0.writeAction("sraddii X16 X17 12 1302")
    tran0.writeAction("yieldt")
    return efa
