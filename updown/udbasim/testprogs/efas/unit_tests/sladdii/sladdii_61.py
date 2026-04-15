from EFA_v2 import *
def sladdii_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3803059362905012621, 14, 1649]
    tran0.writeAction("movir X16 52024")
    tran0.writeAction("slorii X16 X16 12 3354")
    tran0.writeAction("slorii X16 X16 12 2222")
    tran0.writeAction("slorii X16 X16 12 1324")
    tran0.writeAction("slorii X16 X16 12 1651")
    tran0.writeAction("sladdii X16 X17 14 1649")
    tran0.writeAction("yieldt")
    return efa
