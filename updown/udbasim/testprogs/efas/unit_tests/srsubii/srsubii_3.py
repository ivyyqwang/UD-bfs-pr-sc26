from EFA_v2 import *
def srsubii_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8317712756448228352, 8, 1029]
    tran0.writeAction("movir X16 35985")
    tran0.writeAction("slorii X16 X16 12 2245")
    tran0.writeAction("slorii X16 X16 12 304")
    tran0.writeAction("slorii X16 X16 12 688")
    tran0.writeAction("slorii X16 X16 12 3072")
    tran0.writeAction("srsubii X16 X17 8 1029")
    tran0.writeAction("yieldt")
    return efa
