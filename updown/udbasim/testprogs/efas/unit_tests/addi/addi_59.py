from EFA_v2 import *
def addi_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6272202864063035199, 10277]
    tran0.writeAction("movir X16 43252")
    tran0.writeAction("slorii X16 X16 12 2699")
    tran0.writeAction("slorii X16 X16 12 2568")
    tran0.writeAction("slorii X16 X16 12 1372")
    tran0.writeAction("slorii X16 X16 12 2241")
    tran0.writeAction("addi X16 X17 10277")
    tran0.writeAction("yieldt")
    return efa
