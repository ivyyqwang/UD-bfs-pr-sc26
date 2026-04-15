from EFA_v2 import *
def addi_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5745786876634532328, -27012]
    tran0.writeAction("movir X16 20413")
    tran0.writeAction("slorii X16 X16 12 555")
    tran0.writeAction("slorii X16 X16 12 2248")
    tran0.writeAction("slorii X16 X16 12 3696")
    tran0.writeAction("slorii X16 X16 12 2536")
    tran0.writeAction("addi X16 X17 -27012")
    tran0.writeAction("yieldt")
    return efa
