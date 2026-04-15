from EFA_v2 import *
def fcnvt_64_32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7451933947937470263]
    tran0.writeAction("movir X16 26474")
    tran0.writeAction("slorii X16 X16 12 2407")
    tran0.writeAction("slorii X16 X16 12 400")
    tran0.writeAction("slorii X16 X16 12 1995")
    tran0.writeAction("slorii X16 X16 12 1847")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
