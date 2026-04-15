from EFA_v2 import *
def slsubii_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4427200906580765344, 0, 482]
    tran0.writeAction("movir X16 15728")
    tran0.writeAction("slorii X16 X16 12 2364")
    tran0.writeAction("slorii X16 X16 12 1194")
    tran0.writeAction("slorii X16 X16 12 138")
    tran0.writeAction("slorii X16 X16 12 2720")
    tran0.writeAction("slsubii X16 X17 0 482")
    tran0.writeAction("yieldt")
    return efa
