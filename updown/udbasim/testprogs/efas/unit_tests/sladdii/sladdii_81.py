from EFA_v2 import *
def sladdii_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3947199869188346920, 13, 16]
    tran0.writeAction("movir X16 51512")
    tran0.writeAction("slorii X16 X16 12 2986")
    tran0.writeAction("slorii X16 X16 12 467")
    tran0.writeAction("slorii X16 X16 12 2294")
    tran0.writeAction("slorii X16 X16 12 3032")
    tran0.writeAction("sladdii X16 X17 13 16")
    tran0.writeAction("yieldt")
    return efa
