from EFA_v2 import *
def srsubii_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4601438087527986079, 14, 3]
    tran0.writeAction("movir X16 16347")
    tran0.writeAction("slorii X16 X16 12 2424")
    tran0.writeAction("slorii X16 X16 12 4007")
    tran0.writeAction("slorii X16 X16 12 239")
    tran0.writeAction("slorii X16 X16 12 927")
    tran0.writeAction("srsubii X16 X17 14 3")
    tran0.writeAction("yieldt")
    return efa
