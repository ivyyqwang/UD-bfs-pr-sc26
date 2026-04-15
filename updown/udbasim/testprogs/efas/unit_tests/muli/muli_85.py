from EFA_v2 import *
def muli_85():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6150282200400011282, -17390]
    tran0.writeAction("movir X16 21850")
    tran0.writeAction("slorii X16 X16 12 785")
    tran0.writeAction("slorii X16 X16 12 863")
    tran0.writeAction("slorii X16 X16 12 1026")
    tran0.writeAction("slorii X16 X16 12 18")
    tran0.writeAction("muli X16 X17 -17390")
    tran0.writeAction("yieldt")
    return efa
