from EFA_v2 import *
def srsubii_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1337724490341600771, 6, 398]
    tran0.writeAction("movir X16 60783")
    tran0.writeAction("slorii X16 X16 12 1834")
    tran0.writeAction("slorii X16 X16 12 2529")
    tran0.writeAction("slorii X16 X16 12 3475")
    tran0.writeAction("slorii X16 X16 12 509")
    tran0.writeAction("srsubii X16 X17 6 398")
    tran0.writeAction("yieldt")
    return efa
