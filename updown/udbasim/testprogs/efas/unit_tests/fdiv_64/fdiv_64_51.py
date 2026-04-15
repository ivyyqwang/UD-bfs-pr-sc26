from EFA_v2 import *
def fdiv_64_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8765517318930849124, 8069444229775631070]
    tran0.writeAction("movir X16 31141")
    tran0.writeAction("slorii X16 X16 12 1528")
    tran0.writeAction("slorii X16 X16 12 3923")
    tran0.writeAction("slorii X16 X16 12 1669")
    tran0.writeAction("slorii X16 X16 12 3428")
    tran0.writeAction("movir X17 28668")
    tran0.writeAction("slorii X17 X17 12 1740")
    tran0.writeAction("slorii X17 X17 12 1522")
    tran0.writeAction("slorii X17 X17 12 2466")
    tran0.writeAction("slorii X17 X17 12 734")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
