from EFA_v2 import *
def divi_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4904604699152845143, 28673]
    tran0.writeAction("movir X16 48111")
    tran0.writeAction("slorii X16 X16 12 1408")
    tran0.writeAction("slorii X16 X16 12 775")
    tran0.writeAction("slorii X16 X16 12 1159")
    tran0.writeAction("slorii X16 X16 12 1705")
    tran0.writeAction("divi X16 X17 28673")
    tran0.writeAction("yieldt")
    return efa
