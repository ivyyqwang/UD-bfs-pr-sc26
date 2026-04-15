from EFA_v2 import *
def sraddii_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8213300822047796453, 7, 1148]
    tran0.writeAction("movir X16 29179")
    tran0.writeAction("slorii X16 X16 12 2073")
    tran0.writeAction("slorii X16 X16 12 1259")
    tran0.writeAction("slorii X16 X16 12 2386")
    tran0.writeAction("slorii X16 X16 12 3301")
    tran0.writeAction("sraddii X16 X17 7 1148")
    tran0.writeAction("yieldt")
    return efa
