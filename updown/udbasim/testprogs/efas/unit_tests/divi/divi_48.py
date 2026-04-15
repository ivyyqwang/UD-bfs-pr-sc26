from EFA_v2 import *
def divi_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2637309999244941465, 22876]
    tran0.writeAction("movir X16 9369")
    tran0.writeAction("slorii X16 X16 12 2487")
    tran0.writeAction("slorii X16 X16 12 2211")
    tran0.writeAction("slorii X16 X16 12 2377")
    tran0.writeAction("slorii X16 X16 12 2201")
    tran0.writeAction("divi X16 X17 22876")
    tran0.writeAction("yieldt")
    return efa
