from EFA_v2 import *
def slsubii_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1734089511951673164, 12, 1593]
    tran0.writeAction("movir X16 6160")
    tran0.writeAction("slorii X16 X16 12 2963")
    tran0.writeAction("slorii X16 X16 12 2360")
    tran0.writeAction("slorii X16 X16 12 2498")
    tran0.writeAction("slorii X16 X16 12 1868")
    tran0.writeAction("slsubii X16 X17 12 1593")
    tran0.writeAction("yieldt")
    return efa
