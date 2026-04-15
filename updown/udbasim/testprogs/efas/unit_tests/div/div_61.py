from EFA_v2 import *
def div_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-926394433002464739, -5152874656060372429]
    tran0.writeAction("movir X16 62244")
    tran0.writeAction("slorii X16 X16 12 3218")
    tran0.writeAction("slorii X16 X16 12 3042")
    tran0.writeAction("slorii X16 X16 12 4049")
    tran0.writeAction("slorii X16 X16 12 2589")
    tran0.writeAction("movir X17 47229")
    tran0.writeAction("slorii X17 X17 12 1276")
    tran0.writeAction("slorii X17 X17 12 3369")
    tran0.writeAction("slorii X17 X17 12 1672")
    tran0.writeAction("slorii X17 X17 12 2611")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
