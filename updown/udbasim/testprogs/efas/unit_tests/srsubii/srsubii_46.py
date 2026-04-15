from EFA_v2 import *
def srsubii_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1671666914466498385, 10, 1663]
    tran0.writeAction("movir X16 5938")
    tran0.writeAction("slorii X16 X16 12 3907")
    tran0.writeAction("slorii X16 X16 12 939")
    tran0.writeAction("slorii X16 X16 12 2248")
    tran0.writeAction("slorii X16 X16 12 1873")
    tran0.writeAction("srsubii X16 X17 10 1663")
    tran0.writeAction("yieldt")
    return efa
