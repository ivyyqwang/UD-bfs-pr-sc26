from EFA_v2 import *
def srsubii_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1853599567548365167, 3, 1343]
    tran0.writeAction("movir X16 58950")
    tran0.writeAction("slorii X16 X16 12 2832")
    tran0.writeAction("slorii X16 X16 12 924")
    tran0.writeAction("slorii X16 X16 12 1892")
    tran0.writeAction("slorii X16 X16 12 1681")
    tran0.writeAction("srsubii X16 X17 3 1343")
    tran0.writeAction("yieldt")
    return efa
