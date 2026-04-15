from EFA_v2 import *
def srsubii_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2493633341686461588, 0, 834]
    tran0.writeAction("movir X16 56676")
    tran0.writeAction("slorii X16 X16 12 3419")
    tran0.writeAction("slorii X16 X16 12 4")
    tran0.writeAction("slorii X16 X16 12 2900")
    tran0.writeAction("slorii X16 X16 12 2924")
    tran0.writeAction("srsubii X16 X17 0 834")
    tran0.writeAction("yieldt")
    return efa
