from EFA_v2 import *
def sraddii_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6709604060603632558, 3, 1817]
    tran0.writeAction("movir X16 41698")
    tran0.writeAction("slorii X16 X16 12 2858")
    tran0.writeAction("slorii X16 X16 12 2024")
    tran0.writeAction("slorii X16 X16 12 827")
    tran0.writeAction("slorii X16 X16 12 1106")
    tran0.writeAction("sraddii X16 X17 3 1817")
    tran0.writeAction("yieldt")
    return efa
