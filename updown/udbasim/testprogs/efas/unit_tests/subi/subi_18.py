from EFA_v2 import *
def subi_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2532821161612048656, -5500]
    tran0.writeAction("movir X16 8998")
    tran0.writeAction("slorii X16 X16 12 1590")
    tran0.writeAction("slorii X16 X16 12 3409")
    tran0.writeAction("slorii X16 X16 12 1959")
    tran0.writeAction("slorii X16 X16 12 2320")
    tran0.writeAction("subi X16 X17 -5500")
    tran0.writeAction("yieldt")
    return efa
