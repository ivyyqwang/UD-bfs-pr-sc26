from EFA_v2 import *
def sladdii_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6021600827457322620, 2, 147]
    tran0.writeAction("movir X16 44142")
    tran0.writeAction("slorii X16 X16 12 3999")
    tran0.writeAction("slorii X16 X16 12 900")
    tran0.writeAction("slorii X16 X16 12 852")
    tran0.writeAction("slorii X16 X16 12 388")
    tran0.writeAction("sladdii X16 X17 2 147")
    tran0.writeAction("yieldt")
    return efa
