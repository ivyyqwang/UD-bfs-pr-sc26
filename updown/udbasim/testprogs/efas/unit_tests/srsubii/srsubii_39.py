from EFA_v2 import *
def srsubii_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8079172262627959570, 0, 1450]
    tran0.writeAction("movir X16 28702")
    tran0.writeAction("slorii X16 X16 12 4037")
    tran0.writeAction("slorii X16 X16 12 3609")
    tran0.writeAction("slorii X16 X16 12 526")
    tran0.writeAction("slorii X16 X16 12 786")
    tran0.writeAction("srsubii X16 X17 0 1450")
    tran0.writeAction("yieldt")
    return efa
