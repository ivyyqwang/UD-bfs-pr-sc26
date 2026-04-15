from EFA_v2 import *
def sladdii_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5605834550002471381, 8, 1631]
    tran0.writeAction("movir X16 19915")
    tran0.writeAction("slorii X16 X16 12 3789")
    tran0.writeAction("slorii X16 X16 12 638")
    tran0.writeAction("slorii X16 X16 12 2085")
    tran0.writeAction("slorii X16 X16 12 469")
    tran0.writeAction("sladdii X16 X17 8 1631")
    tran0.writeAction("yieldt")
    return efa
