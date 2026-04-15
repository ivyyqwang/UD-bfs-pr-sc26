from EFA_v2 import *
def slsubii_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3215722307975269547, 9, 521]
    tran0.writeAction("movir X16 54111")
    tran0.writeAction("slorii X16 X16 12 1881")
    tran0.writeAction("slorii X16 X16 12 2360")
    tran0.writeAction("slorii X16 X16 12 3419")
    tran0.writeAction("slorii X16 X16 12 853")
    tran0.writeAction("slsubii X16 X17 9 521")
    tran0.writeAction("yieldt")
    return efa
