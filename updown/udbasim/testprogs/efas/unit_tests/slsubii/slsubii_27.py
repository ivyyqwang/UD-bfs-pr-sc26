from EFA_v2 import *
def slsubii_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8259087764179637831, 6, 1657]
    tran0.writeAction("movir X16 36193")
    tran0.writeAction("slorii X16 X16 12 3382")
    tran0.writeAction("slorii X16 X16 12 4063")
    tran0.writeAction("slorii X16 X16 12 1218")
    tran0.writeAction("slorii X16 X16 12 2489")
    tran0.writeAction("slsubii X16 X17 6 1657")
    tran0.writeAction("yieldt")
    return efa
