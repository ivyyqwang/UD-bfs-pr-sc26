from EFA_v2 import *
def srsubii_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7902784932440433795, 8, 790]
    tran0.writeAction("movir X16 28076")
    tran0.writeAction("slorii X16 X16 12 1360")
    tran0.writeAction("slorii X16 X16 12 1658")
    tran0.writeAction("slorii X16 X16 12 1726")
    tran0.writeAction("slorii X16 X16 12 1155")
    tran0.writeAction("srsubii X16 X17 8 790")
    tran0.writeAction("yieldt")
    return efa
