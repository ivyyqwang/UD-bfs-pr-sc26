from EFA_v2 import *
def muli_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3943300714400226697, 2128]
    tran0.writeAction("movir X16 51526")
    tran0.writeAction("slorii X16 X16 12 2382")
    tran0.writeAction("slorii X16 X16 12 1163")
    tran0.writeAction("slorii X16 X16 12 2582")
    tran0.writeAction("slorii X16 X16 12 631")
    tran0.writeAction("muli X16 X17 2128")
    tran0.writeAction("yieldt")
    return efa
