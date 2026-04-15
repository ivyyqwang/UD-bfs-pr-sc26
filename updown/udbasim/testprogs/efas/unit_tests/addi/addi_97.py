from EFA_v2 import *
def addi_97():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1754070691391976223, 23507]
    tran0.writeAction("movir X16 59304")
    tran0.writeAction("slorii X16 X16 12 1183")
    tran0.writeAction("slorii X16 X16 12 4072")
    tran0.writeAction("slorii X16 X16 12 2692")
    tran0.writeAction("slorii X16 X16 12 3297")
    tran0.writeAction("addi X16 X17 23507")
    tran0.writeAction("yieldt")
    return efa
