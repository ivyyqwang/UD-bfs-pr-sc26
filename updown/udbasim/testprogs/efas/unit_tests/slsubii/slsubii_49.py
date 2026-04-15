from EFA_v2 import *
def slsubii_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6569656651101462069, 6, 1156]
    tran0.writeAction("movir X16 23340")
    tran0.writeAction("slorii X16 X16 12 446")
    tran0.writeAction("slorii X16 X16 12 2729")
    tran0.writeAction("slorii X16 X16 12 757")
    tran0.writeAction("slorii X16 X16 12 3637")
    tran0.writeAction("slsubii X16 X17 6 1156")
    tran0.writeAction("yieldt")
    return efa
