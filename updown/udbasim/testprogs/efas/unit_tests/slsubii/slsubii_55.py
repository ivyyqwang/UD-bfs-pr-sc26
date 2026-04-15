from EFA_v2 import *
def slsubii_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1547291141702232471, 7, 1619]
    tran0.writeAction("movir X16 60038")
    tran0.writeAction("slorii X16 X16 12 3758")
    tran0.writeAction("slorii X16 X16 12 1934")
    tran0.writeAction("slorii X16 X16 12 2989")
    tran0.writeAction("slorii X16 X16 12 1641")
    tran0.writeAction("slsubii X16 X17 7 1619")
    tran0.writeAction("yieldt")
    return efa
