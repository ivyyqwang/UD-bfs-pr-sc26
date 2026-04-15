from EFA_v2 import *
def srsubii_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5536273592293047405, 7, 75]
    tran0.writeAction("movir X16 45867")
    tran0.writeAction("slorii X16 X16 12 840")
    tran0.writeAction("slorii X16 X16 12 15")
    tran0.writeAction("slorii X16 X16 12 4084")
    tran0.writeAction("slorii X16 X16 12 915")
    tran0.writeAction("srsubii X16 X17 7 75")
    tran0.writeAction("yieldt")
    return efa
