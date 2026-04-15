from EFA_v2 import *
def addi_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5638938831454433736, 22110]
    tran0.writeAction("movir X16 20033")
    tran0.writeAction("slorii X16 X16 12 2191")
    tran0.writeAction("slorii X16 X16 12 3494")
    tran0.writeAction("slorii X16 X16 12 4087")
    tran0.writeAction("slorii X16 X16 12 456")
    tran0.writeAction("addi X16 X17 22110")
    tran0.writeAction("yieldt")
    return efa
