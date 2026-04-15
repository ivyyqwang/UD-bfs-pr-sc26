from EFA_v2 import *
def sraddii_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2717265783320078802, 5, 789]
    tran0.writeAction("movir X16 9653")
    tran0.writeAction("slorii X16 X16 12 2733")
    tran0.writeAction("slorii X16 X16 12 1359")
    tran0.writeAction("slorii X16 X16 12 478")
    tran0.writeAction("slorii X16 X16 12 2514")
    tran0.writeAction("sraddii X16 X17 5 789")
    tran0.writeAction("yieldt")
    return efa
