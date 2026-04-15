from EFA_v2 import *
def addi_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8319214284230656177, 27353]
    tran0.writeAction("movir X16 35980")
    tran0.writeAction("slorii X16 X16 12 874")
    tran0.writeAction("slorii X16 X16 12 3970")
    tran0.writeAction("slorii X16 X16 12 311")
    tran0.writeAction("slorii X16 X16 12 3919")
    tran0.writeAction("addi X16 X17 27353")
    tran0.writeAction("yieldt")
    return efa
