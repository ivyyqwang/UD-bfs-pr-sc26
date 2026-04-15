from EFA_v2 import *
def slsubii_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5862181498914716074, 10, 1883]
    tran0.writeAction("movir X16 44709")
    tran0.writeAction("slorii X16 X16 12 1423")
    tran0.writeAction("slorii X16 X16 12 3172")
    tran0.writeAction("slorii X16 X16 12 1316")
    tran0.writeAction("slorii X16 X16 12 1622")
    tran0.writeAction("slsubii X16 X17 10 1883")
    tran0.writeAction("yieldt")
    return efa
