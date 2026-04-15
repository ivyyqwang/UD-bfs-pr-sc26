from EFA_v2 import *
def slsubii_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5687427159032108210, 6, 932]
    tran0.writeAction("movir X16 20205")
    tran0.writeAction("slorii X16 X16 12 3277")
    tran0.writeAction("slorii X16 X16 12 3628")
    tran0.writeAction("slorii X16 X16 12 73")
    tran0.writeAction("slorii X16 X16 12 1202")
    tran0.writeAction("slsubii X16 X17 6 932")
    tran0.writeAction("yieldt")
    return efa
