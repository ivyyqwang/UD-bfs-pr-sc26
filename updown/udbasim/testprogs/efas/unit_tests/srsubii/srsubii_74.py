from EFA_v2 import *
def srsubii_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [603499952171381146, 7, 134]
    tran0.writeAction("movir X16 2144")
    tran0.writeAction("slorii X16 X16 12 256")
    tran0.writeAction("slorii X16 X16 12 591")
    tran0.writeAction("slorii X16 X16 12 575")
    tran0.writeAction("slorii X16 X16 12 410")
    tran0.writeAction("srsubii X16 X17 7 134")
    tran0.writeAction("yieldt")
    return efa
