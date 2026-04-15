from EFA_v2 import *
def sladdii_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9171666732461937587, 8, 1699]
    tran0.writeAction("movir X16 32584")
    tran0.writeAction("slorii X16 X16 12 1252")
    tran0.writeAction("slorii X16 X16 12 3250")
    tran0.writeAction("slorii X16 X16 12 2709")
    tran0.writeAction("slorii X16 X16 12 947")
    tran0.writeAction("sladdii X16 X17 8 1699")
    tran0.writeAction("yieldt")
    return efa
