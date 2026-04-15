from EFA_v2 import *
def addi_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5742437044144108965, 16718]
    tran0.writeAction("movir X16 45134")
    tran0.writeAction("slorii X16 X16 12 3134")
    tran0.writeAction("slorii X16 X16 12 3806")
    tran0.writeAction("slorii X16 X16 12 3056")
    tran0.writeAction("slorii X16 X16 12 2651")
    tran0.writeAction("addi X16 X17 16718")
    tran0.writeAction("yieldt")
    return efa
