from EFA_v2 import *
def addi_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8753535879186243771, 26423]
    tran0.writeAction("movir X16 34437")
    tran0.writeAction("slorii X16 X16 12 791")
    tran0.writeAction("slorii X16 X16 12 3840")
    tran0.writeAction("slorii X16 X16 12 1913")
    tran0.writeAction("slorii X16 X16 12 3909")
    tran0.writeAction("addi X16 X17 26423")
    tran0.writeAction("yieldt")
    return efa
