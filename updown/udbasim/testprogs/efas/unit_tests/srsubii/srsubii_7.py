from EFA_v2 import *
def srsubii_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-289846672097053865, 4, 1062]
    tran0.writeAction("movir X16 64506")
    tran0.writeAction("slorii X16 X16 12 1055")
    tran0.writeAction("slorii X16 X16 12 3270")
    tran0.writeAction("slorii X16 X16 12 1335")
    tran0.writeAction("slorii X16 X16 12 855")
    tran0.writeAction("srsubii X16 X17 4 1062")
    tran0.writeAction("yieldt")
    return efa
