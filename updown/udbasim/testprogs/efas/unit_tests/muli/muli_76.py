from EFA_v2 import *
def muli_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3086973338282320297, -26707]
    tran0.writeAction("movir X16 54568")
    tran0.writeAction("slorii X16 X16 12 3553")
    tran0.writeAction("slorii X16 X16 12 2740")
    tran0.writeAction("slorii X16 X16 12 2377")
    tran0.writeAction("slorii X16 X16 12 3671")
    tran0.writeAction("muli X16 X17 -26707")
    tran0.writeAction("yieldt")
    return efa
