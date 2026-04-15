from EFA_v2 import *
def sladdii_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [561560750947437601, 7, 1317]
    tran0.writeAction("movir X16 1995")
    tran0.writeAction("slorii X16 X16 12 264")
    tran0.writeAction("slorii X16 X16 12 1816")
    tran0.writeAction("slorii X16 X16 12 96")
    tran0.writeAction("slorii X16 X16 12 3105")
    tran0.writeAction("sladdii X16 X17 7 1317")
    tran0.writeAction("yieldt")
    return efa
