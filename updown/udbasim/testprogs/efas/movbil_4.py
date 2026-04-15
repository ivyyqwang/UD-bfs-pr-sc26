from EFA_v2 import *
def movbil_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 114")
    tran0.writeAction("slorii X16 X16 12 2639")
    tran0.writeAction("addi X16 X21 0")
    tran0.writeAction("sli X7 X19 3")
    tran0.writeAction("add X16 X19 X16")
    tran0.writeAction("movbil X16 6 163")
    tran0.writeAction("yieldt")
    return efa
