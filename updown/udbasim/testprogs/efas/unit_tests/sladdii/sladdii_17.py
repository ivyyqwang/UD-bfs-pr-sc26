from EFA_v2 import *
def sladdii_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2960902713858211326, 7, 1097]
    tran0.writeAction("movir X16 55016")
    tran0.writeAction("slorii X16 X16 12 3114")
    tran0.writeAction("slorii X16 X16 12 2901")
    tran0.writeAction("slorii X16 X16 12 4060")
    tran0.writeAction("slorii X16 X16 12 514")
    tran0.writeAction("sladdii X16 X17 7 1097")
    tran0.writeAction("yieldt")
    return efa
