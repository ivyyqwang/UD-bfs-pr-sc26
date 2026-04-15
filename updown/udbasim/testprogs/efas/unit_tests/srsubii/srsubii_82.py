from EFA_v2 import *
def srsubii_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8240958308315880459, 12, 1343]
    tran0.writeAction("movir X16 36258")
    tran0.writeAction("slorii X16 X16 12 961")
    tran0.writeAction("slorii X16 X16 12 1216")
    tran0.writeAction("slorii X16 X16 12 114")
    tran0.writeAction("slorii X16 X16 12 1013")
    tran0.writeAction("srsubii X16 X17 12 1343")
    tran0.writeAction("yieldt")
    return efa
