from EFA_v2 import *
def slsubii_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7980214421716685761, 5, 1875]
    tran0.writeAction("movir X16 37184")
    tran0.writeAction("slorii X16 X16 12 2388")
    tran0.writeAction("slorii X16 X16 12 946")
    tran0.writeAction("slorii X16 X16 12 522")
    tran0.writeAction("slorii X16 X16 12 3135")
    tran0.writeAction("slsubii X16 X17 5 1875")
    tran0.writeAction("yieldt")
    return efa
