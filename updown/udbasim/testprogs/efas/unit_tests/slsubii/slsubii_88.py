from EFA_v2 import *
def slsubii_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7523804447964735737, 5, 1021]
    tran0.writeAction("movir X16 26729")
    tran0.writeAction("slorii X16 X16 12 3780")
    tran0.writeAction("slorii X16 X16 12 2136")
    tran0.writeAction("slorii X16 X16 12 1810")
    tran0.writeAction("slorii X16 X16 12 2297")
    tran0.writeAction("slsubii X16 X17 5 1021")
    tran0.writeAction("yieldt")
    return efa
