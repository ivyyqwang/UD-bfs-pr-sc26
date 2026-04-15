from EFA_v2 import *
def srsubii_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6952571982808141110, 12, 1072]
    tran0.writeAction("movir X16 24700")
    tran0.writeAction("slorii X16 X16 12 2038")
    tran0.writeAction("slorii X16 X16 12 462")
    tran0.writeAction("slorii X16 X16 12 2508")
    tran0.writeAction("slorii X16 X16 12 3382")
    tran0.writeAction("srsubii X16 X17 12 1072")
    tran0.writeAction("yieldt")
    return efa
