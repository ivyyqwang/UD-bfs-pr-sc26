from EFA_v2 import *
def srsubii_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4413623595135642694, 0, 1519]
    tran0.writeAction("movir X16 49855")
    tran0.writeAction("slorii X16 X16 12 2699")
    tran0.writeAction("slorii X16 X16 12 2431")
    tran0.writeAction("slorii X16 X16 12 2693")
    tran0.writeAction("slorii X16 X16 12 954")
    tran0.writeAction("srsubii X16 X17 0 1519")
    tran0.writeAction("yieldt")
    return efa
