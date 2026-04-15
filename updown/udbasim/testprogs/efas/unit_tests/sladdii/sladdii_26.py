from EFA_v2 import *
def sladdii_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2147235392795160223, 13, 729]
    tran0.writeAction("movir X16 7628")
    tran0.writeAction("slorii X16 X16 12 2099")
    tran0.writeAction("slorii X16 X16 12 1684")
    tran0.writeAction("slorii X16 X16 12 2874")
    tran0.writeAction("slorii X16 X16 12 3743")
    tran0.writeAction("sladdii X16 X17 13 729")
    tran0.writeAction("yieldt")
    return efa
