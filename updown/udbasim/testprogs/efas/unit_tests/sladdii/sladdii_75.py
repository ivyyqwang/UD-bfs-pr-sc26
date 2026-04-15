from EFA_v2 import *
def sladdii_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7132808602574603761, 11, 162]
    tran0.writeAction("movir X16 25340")
    tran0.writeAction("slorii X16 X16 12 3386")
    tran0.writeAction("slorii X16 X16 12 511")
    tran0.writeAction("slorii X16 X16 12 1268")
    tran0.writeAction("slorii X16 X16 12 1521")
    tran0.writeAction("sladdii X16 X17 11 162")
    tran0.writeAction("yieldt")
    return efa
