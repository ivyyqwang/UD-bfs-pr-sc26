from EFA_v2 import *
def slsubii_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8730494543599759896, 6, 1637]
    tran0.writeAction("movir X16 31016")
    tran0.writeAction("slorii X16 X16 12 3880")
    tran0.writeAction("slorii X16 X16 12 2048")
    tran0.writeAction("slorii X16 X16 12 3071")
    tran0.writeAction("slorii X16 X16 12 536")
    tran0.writeAction("slsubii X16 X17 6 1637")
    tran0.writeAction("yieldt")
    return efa
