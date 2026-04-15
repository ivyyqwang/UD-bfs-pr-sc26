from EFA_v2 import *
def srsubii_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1613326892638128134, 4, 947]
    tran0.writeAction("movir X16 5731")
    tran0.writeAction("slorii X16 X16 12 2820")
    tran0.writeAction("slorii X16 X16 12 726")
    tran0.writeAction("slorii X16 X16 12 1148")
    tran0.writeAction("slorii X16 X16 12 2054")
    tran0.writeAction("srsubii X16 X17 4 947")
    tran0.writeAction("yieldt")
    return efa
